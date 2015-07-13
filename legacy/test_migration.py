import comissoes
import materia
from .migration import appconfs, get_renames, legacy_app


RENAMING_IGNORED_MODELS = [
    comissoes.models.Composicao,
]

RENAMING_IGNORED_FIELDS = [
    (materia.models.Proposicao, {'documento'}),
    (materia.models.TipoProposicao, {'tipo_documento'}),
]


def test_get_renames():
    field_renames, model_renames = get_renames()
    all_models = {m for ac in appconfs for m in ac.get_models()}
    for model in all_models:
        field_names = {f.name for f in model._meta.fields if f.name != 'id'}
        if model not in field_renames:
            # check ignored models in renaming
            assert model in RENAMING_IGNORED_MODELS
        else:
            renamed = set(field_renames[model].keys())

            # all renamed field references correspond to an actual field
            assert renamed <= field_names

            # check ignored fields in renaming
            missing_in_renames = field_names - renamed
            if missing_in_renames:
                assert (model, missing_in_renames) in RENAMING_IGNORED_FIELDS

            # all old names correspond to a legacy model field
            legacy_model = legacy_app.get_model(model_renames.get(model, model.__name__))
            assert set(field_renames[model].values()) <= {f.name for f in legacy_model._meta.fields}

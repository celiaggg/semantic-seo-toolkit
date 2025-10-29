from semantic_seo.shared.config.loader import load_config


def test_load_config_defaults():
    cfg = load_config(load_env=False)
    assert cfg.project.name == "semantic-seo"
    assert cfg.embeddings.model_name

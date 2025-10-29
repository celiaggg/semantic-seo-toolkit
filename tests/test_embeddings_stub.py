import pytest

try:
    from semantic_seo.stage5.embeddings.embedder import SentenceTransformerEmbedder
    _HAVE_ST = True
except Exception:
    _HAVE_ST = False


@pytest.mark.skipif(not _HAVE_ST, reason="sentence-transformers not installed")
def test_embedder_runs():
    emb = SentenceTransformerEmbedder()
    vecs = emb.embed_texts(["hello world"]) 
    assert isinstance(vecs, list) and len(vecs) == 1 and isinstance(vecs[0], list)

"""Schema smoke tests for Phase 2 database models."""

from neurorag.database.models import Base, Document, Embedding, QueryLog


def test_phase2_tables_registered_in_metadata() -> None:
    table_names = set(Base.metadata.tables)

    assert Document.__tablename__ == "documents"
    assert Embedding.__tablename__ == "embeddings"
    assert QueryLog.__tablename__ == "query_logs"
    assert {"documents", "embeddings", "query_logs"}.issubset(table_names)


def test_embedding_vector_dimension_is_768() -> None:
    vector_type = Embedding.__table__.c.embedding.type

    assert getattr(vector_type, "dim", None) == 768


def test_embedding_foreign_key_targets_documents() -> None:
    fk_targets = {fk.target_fullname for fk in Embedding.__table__.c.document_id.foreign_keys}

    assert "documents.id" in fk_targets

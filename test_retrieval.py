from agents.retrieval_agent import retrieve_context


def test_retrieve_context_exists():
    assert callable(retrieve_context)

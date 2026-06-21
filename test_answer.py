from agents.answer_agent import generate_answer


def test_generate_answer_exists():
    assert callable(generate_answer)

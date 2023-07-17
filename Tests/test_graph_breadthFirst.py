import pytest
from CC.graphs.graph_breadthFirst import Graph


def test_breadth_first():
    graph = Graph()
    graph.add_node("Pandora")
    graph.add_node("Arendelle")
    graph.add_node("Metroville")
    graph.add_node("Monstroplolis")
    graph.add_node("Narnia")
    graph.add_node("Naboo")

    graph.add_edge("Pandora", "Arendelle")
    graph.add_edge("Arendelle", "Metroville")
    graph.add_edge("Arendelle", "Monstroplolis")
    graph.add_edge("Metroville", "Narnia")
    graph.add_edge("Metroville", "Naboo")

    assert graph.breadth_first("Pandora") == [
        "Pandora",
        "Arendelle",
        "Metroville",
        "Monstroplolis",
        "Narnia",
        "Naboo",
    ]
    assert graph.breadth_first("Arendelle") == [
        "Arendelle",
        "Pandora",
        "Metroville",
        "Monstroplolis",
        "Narnia",
        "Naboo",
    ]

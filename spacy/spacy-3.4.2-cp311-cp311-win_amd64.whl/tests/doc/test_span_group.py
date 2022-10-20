import pytest
from random import Random
from spacy.matcher import Matcher
from spacy.tokens import Span, SpanGroup


@pytest.fixture
def doc(en_tokenizer):
    doc = en_tokenizer("0 1 2 3 4 5 6")
    matcher = Matcher(en_tokenizer.vocab, validate=True)

    # fmt: off
    matcher.add("4", [[{}, {}, {}, {}]])
    matcher.add("2", [[{}, {}, ]])
    matcher.add("1", [[{}, ]])
    # fmt: on
    matches = matcher(doc)
    spans = []
    for match in matches:
        spans.append(
            Span(doc, match[1], match[2], en_tokenizer.vocab.strings[match[0]])
        )
    Random(42).shuffle(spans)
    doc.spans["SPANS"] = SpanGroup(
        doc, name="SPANS", attrs={"key": "value"}, spans=spans
    )
    return doc


@pytest.fixture
def other_doc(en_tokenizer):
    doc = en_tokenizer("0 1 2 3 4 5 6")
    matcher = Matcher(en_tokenizer.vocab, validate=True)

    # fmt: off
    matcher.add("4", [[{}, {}, {}, {}]])
    matcher.add("2", [[{}, {}, ]])
    matcher.add("1", [[{}, ]])
    # fmt: on

    matches = matcher(doc)
    spans = []
    for match in matches:
        spans.append(
            Span(doc, match[1], match[2], en_tokenizer.vocab.strings[match[0]])
        )
    Random(42).shuffle(spans)
    doc.spans["SPANS"] = SpanGroup(
        doc, name="SPANS", attrs={"key": "value"}, spans=spans
    )
    return doc


@pytest.fixture
def span_group(en_tokenizer):
    doc = en_tokenizer("0 1 2 3 4 5 6")
    matcher = Matcher(en_tokenizer.vocab, validate=True)

    # fmt: off
    matcher.add("4", [[{}, {}, {}, {}]])
    matcher.add("2", [[{}, {}, ]])
    matcher.add("1", [[{}, ]])
    # fmt: on

    matches = matcher(doc)
    spans = []
    for match in matches:
        spans.append(
            Span(doc, match[1], match[2], en_tokenizer.vocab.strings[match[0]])
        )
    Random(42).shuffle(spans)
    doc.spans["SPANS"] = SpanGroup(
        doc, name="SPANS", attrs={"key": "value"}, spans=spans
    )


def test_span_group_copy(doc):
    span_group = doc.spans["SPANS"]
    clone = span_group.copy()
    assert clone != span_group
    assert clone.name == span_group.name
    assert clone.attrs == span_group.attrs
    assert len(clone) == len(span_group)
    assert list(span_group) == list(clone)
    clone.name = "new_name"
    clone.attrs["key"] = "new_value"
    clone.append(Span(doc, 0, 6, "LABEL"))
    assert clone.name != span_group.name
    assert clone.attrs != span_group.attrs
    assert span_group.attrs["key"] == "value"
    assert list(span_group) != list(clone)


def test_span_group_set_item(doc, other_doc):
    span_group = doc.spans["SPANS"]

    index = 5
    span = span_group[index]
    span.label_ = "NEW LABEL"
    span.kb_id = doc.vocab.strings["KB_ID"]

    assert span_group[index].label != span.label
    assert span_group[index].kb_id != span.kb_id

    span_group[index] = span
    assert span_group[index].start == span.start
    assert span_group[index].end == span.end
    assert span_group[index].label == span.label
    assert span_group[index].kb_id == span.kb_id
    assert span_group[index] == span

    with pytest.raises(IndexError):
        span_group[-100] = span
    with pytest.raises(IndexError):
        span_group[100] = span

    span = Span(other_doc, 0, 2)
    with pytest.raises(ValueError):
        span_group[index] = span


def test_span_group_has_overlap(doc):
    span_group = doc.spans["SPANS"]
    assert span_group.has_overlap


def test_span_group_concat(doc, other_doc):
    span_group_1 = doc.spans["SPANS"]
    spans = [doc[0:5], doc[0:6]]
    span_group_2 = SpanGroup(
        doc,
        name="MORE_SPANS",
        attrs={"key": "new_value", "new_key": "new_value"},
        spans=spans,
    )
    span_group_3 = span_group_1._concat(span_group_2)
    assert span_group_3.name == span_group_1.name
    assert span_group_3.attrs == {"key": "value", "new_key": "new_value"}
    span_list_expected = list(span_group_1) + list(span_group_2)
    assert list(span_group_3) == list(span_list_expected)

    # Inplace
    span_list_expected = list(span_group_1) + list(span_group_2)
    span_group_3 = span_group_1._concat(span_group_2, inplace=True)
    assert span_group_3 == span_group_1
    assert span_group_3.name == span_group_1.name
    assert span_group_3.attrs == {"key": "value", "new_key": "new_value"}
    assert list(span_group_3) == list(span_list_expected)

    span_group_2 = other_doc.spans["SPANS"]
    with pytest.raises(ValueError):
        span_group_1._concat(span_group_2)


def test_span_doc_delitem(doc):
    span_group = doc.spans["SPANS"]
    length = len(span_group)
    index = 5
    span = span_group[index]
    next_span = span_group[index + 1]
    del span_group[index]
    assert len(span_group) == length - 1
    assert span_group[index] != span
    assert span_group[index] == next_span

    with pytest.raises(IndexError):
        del span_group[-100]
    with pytest.raises(IndexError):
        del span_group[100]


def test_span_group_add(doc):
    span_group_1 = doc.spans["SPANS"]
    spans = [doc[0:5], doc[0:6]]
    span_group_2 = SpanGroup(
        doc,
        name="MORE_SPANS",
        attrs={"key": "new_value", "new_key": "new_value"},
        spans=spans,
    )

    span_group_3_expected = span_group_1._concat(span_group_2)

    span_group_3 = span_group_1 + span_group_2
    assert len(span_group_3) == len(span_group_3_expected)
    assert span_group_3.attrs == {"key": "value", "new_key": "new_value"}
    assert list(span_group_3) == list(span_group_3_expected)


def test_span_group_iadd(doc):
    span_group_1 = doc.spans["SPANS"].copy()
    spans = [doc[0:5], doc[0:6]]
    span_group_2 = SpanGroup(
        doc,
        name="MORE_SPANS",
        attrs={"key": "new_value", "new_key": "new_value"},
        spans=spans,
    )

    span_group_1_expected = span_group_1._concat(span_group_2)

    span_group_1 += span_group_2
    assert len(span_group_1) == len(span_group_1_expected)
    assert span_group_1.attrs == {"key": "value", "new_key": "new_value"}
    assert list(span_group_1) == list(span_group_1_expected)

    span_group_1 = doc.spans["SPANS"].copy()
    span_group_1 += spans
    assert len(span_group_1) == len(span_group_1_expected)
    assert span_group_1.attrs == {
        "key": "value",
    }
    assert list(span_group_1) == list(span_group_1_expected)


def test_span_group_extend(doc):
    span_group_1 = doc.spans["SPANS"].copy()
    spans = [doc[0:5], doc[0:6]]
    span_group_2 = SpanGroup(
        doc,
        name="MORE_SPANS",
        attrs={"key": "new_value", "new_key": "new_value"},
        spans=spans,
    )

    span_group_1_expected = span_group_1._concat(span_group_2)

    span_group_1.extend(span_group_2)
    assert len(span_group_1) == len(span_group_1_expected)
    assert span_group_1.attrs == {"key": "value", "new_key": "new_value"}
    assert list(span_group_1) == list(span_group_1_expected)

    span_group_1 = doc.spans["SPANS"]
    span_group_1.extend(spans)
    assert len(span_group_1) == len(span_group_1_expected)
    assert span_group_1.attrs == {"key": "value"}
    assert list(span_group_1) == list(span_group_1_expected)


def test_span_group_dealloc(span_group):
    with pytest.raises(AttributeError):
        print(span_group.doc)

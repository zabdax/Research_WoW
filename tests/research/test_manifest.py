from pathlib import Path

from research.provenance.manifest import create_manifest


def test_manifest_hashes_inputs_and_outputs(tmp_path):
    input_file = tmp_path / "input.txt"; input_file.write_text("input", encoding="utf-8")
    output_file = tmp_path / "output.txt"; output_file.write_text("output", encoding="utf-8")
    manifest = create_manifest(tmp_path / "manifest.json", [input_file], [output_file], seeds=[1, 2])
    assert manifest["seeds"] == [1, 2]
    assert str(input_file) in manifest["inputs"]

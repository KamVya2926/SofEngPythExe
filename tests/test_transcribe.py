import pytest
from unittest.mock import patch
from SEPythExe.modules.transcribe import transcribe_dna_sequence


# Test when the DNA sequence is valid
@pytest.fixture
def mock_valid_dna_rna():
    with patch('SEPythExe.logger') as mock_logger, \
            patch('SEPythExe.utils.validateDNA.validate_dna') as mock_validate_dna, \
            patch('SEPythExe.utils.validateRNA.validate_rna') as mock_validate_rna:
        # Mock responses for validate_dna and validate_rna
        mock_validate_dna.return_value = True  # Valid DNA
        mock_validate_rna.return_value = True  # Valid RNA
        yield mock_logger, mock_validate_dna, mock_validate_rna


def test_transcribe_dna_sequence_valid(mock_valid_dna_rna):
    mock_logger, mock_validate_dna, mock_validate_rna = mock_valid_dna_rna

    # Arrange
    dna_sequence = "ATGCTAGCTA"
    expected_rna_sequence = "augcuaagcu"

    # Act
    rna_sequence = transcribe_dna_sequence(dna_sequence)

    # Assert
    mock_validate_dna.assert_called_once_with(dna_sequence)
    mock_validate_rna.assert_called_once_with(expected_rna_sequence)
    mock_logger.info.assert_any_call('Input is a valid DNA sequence')
    mock_logger.info.assert_any_call('Transcribing DNA sequence to RNA')
    mock_logger.info.assert_any_call(
        f"Successfully transcribed input DNA sequence to a valid RNA sequence: {expected_rna_sequence}")

    # Check that the RNA sequence is correct
    assert rna_sequence == expected_rna_sequence


# Test when the DNA sequence is invalid
@pytest.fixture
def mock_invalid_dna():
    with patch('SEPythExe.logger') as mock_logger, \
            patch('SEPythExe.utils.validateDNA.validate_dna') as mock_validate_dna, \
            patch('SEPythExe.utils.validateRNA.validate_rna') as mock_validate_rna:
        # Mock invalid DNA sequence
        mock_validate_dna.return_value = False  # Invalid DNA
        yield mock_logger, mock_validate_dna, mock_validate_rna


def test_transcribe_dna_sequence_invalid_dna(mock_invalid_dna):
    mock_logger, mock_validate_dna, mock_validate_rna = mock_invalid_dna

    # Arrange
    dna_sequence = "ATGCTXGCTA"  # Invalid DNA sequence with 'X'

    # Act
    rna_sequence = transcribe_dna_sequence(dna_sequence)

    # Assert
    mock_validate_dna.assert_called_once_with(dna_sequence)
    mock_logger.info.assert_any_call('Input is a valid DNA sequence')  # This should still log the info about valid DNA
    mock_validate_rna.assert_not_called()  # No RNA validation should happen

    # The output should be empty because of invalid DNA
    assert rna_sequence == ""


# Test when the RNA sequence is invalid (but DNA is valid)
@pytest.fixture
def mock_invalid_rna():
    with patch('SEPythExe.logger') as mock_logger, \
            patch('SEPythExe.utils.validateDNA.validate_dna') as mock_validate_dna, \
            patch('SEPythExe.utils.validateRNA.validate_rna') as mock_validate_rna:
        mock_validate_dna.return_value = True  # Valid DNA
        mock_validate_rna.return_value = False  # Invalid RNA
        yield mock_logger, mock_validate_dna, mock_validate_rna


def test_transcribe_dna_sequence_invalid_rna(mock_invalid_rna):
    mock_logger, mock_validate_dna, mock_validate_rna = mock_invalid_rna

    # Arrange
    dna_sequence = "ATGCTAGCTA"
    expected_rna_sequence = "augcuaagcu"

    # Act
    rna_sequence = transcribe_dna_sequence(dna_sequence)

    # Assert
    mock_validate_dna.assert_called_once_with(dna_sequence)
    mock_validate_rna.assert_called_once_with(expected_rna_sequence)
    mock_logger.info.assert_any_call('Input is a valid DNA sequence')
    mock_logger.info.assert_any_call('Transcribing DNA sequence to RNA')
    mock_logger.info.assert_any_call(
        f"Successfully transcribed input DNA sequence to a valid RNA sequence: {expected_rna_sequence}")

    # The RNA sequence is still returned, even though it's invalid
    assert rna_sequence == expected_rna_sequence

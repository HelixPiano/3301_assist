import statistics
import helper_functions as hpf


def return_english_text() -> str:
    text = ('HALF FINISH STOOL INJURY CLERK BEARD BUNDLE SOIL STREAM FROWN CRUTCH FAULT ACHIEVEMENT FRAGRANT BRIDGE '
            'STRENGTH COMBINATION GOLF SPEED SMALL PLEDGE COOPERATION HILL MANAGEMENT CULTURE SLEEVE CONCERT CIRCLE '
            'RUMOR AUTOMATIC SMOOTH FAREWELL FUNCTION EXPERIMENT TROPICAL DESPISE MONARCH HEAVEN PUSH PARTICIPATE '
            'PATIENCE SKIP TIMETABLE GRAZE BRUSH HANDY SICK LINGER DIFFICULT FILM QUESTION')
    return text


def create_english_statistics():
    text = return_english_text()
    num_words = statistics.count_words()
    english_to_indices = hpf.convert_text_to_index(text)
    english_to_runes
    ioc
    quadgrams

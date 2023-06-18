
def possible_options(option: str):
    possible_options = ("1", "clima", "clima atual", "2", "previsão",
                        "previsao", "previsão do tempo",
                        "previsao do tempo")
    return option in possible_options


def which_option(option):
    current_weather_options = ("1", "clima", "clima atual")

    forecast_options = ("2", "previsão", "previsao", "previsão do tempo",
                        "previsao do tempo")
    if option in current_weather_options:
        return "1"

    if option in forecast_options:
        return "2"


def user_input():
    option = input("Bem vindo à WeatherAPI, o que deseja fazer?"
                   "[1] Clima atual" "[2] Previsão do tempo"
                   ).lower().strip()

    if not possible_options(option):
        raise ValueError("Por favor, digite uma opção válida")

    return which_option(option)

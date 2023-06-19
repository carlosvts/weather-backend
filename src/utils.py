def possible_options(option: str):
    possible_options = ("1", "clima", "clima atual", "2", "previsão",
                        "previsao", "previsão do tempo",
                        "previsao do tempo")
    return option in possible_options


def which_option(option):
    """
    Parse if user wants weather info(1) or forecast info(2)
    :param str option: input option gived by the user 
    """
    current_weather_options = ("1", "clima", "clima atual")

    forecast_options = ("2", "previsão", "previsao", "previsão do tempo",
                        "previsao do tempo")
    if option in current_weather_options:
        return "1"

    if option in forecast_options:
        return "2"


def user_input():
    option = input("Bem vindo à WeatherAPI, o que deseja fazer?"
                   "[1] Clima atual" "[2] Previsão do tempo "
                   ).lower().strip()

    if not possible_options(option):
        raise ValueError("Por favor, digite uma opção válida")

    return which_option(option)


def current_weather_localization_input():
    param = input("Ok! Informe a localização: ")
    return param


def weather_response_options(location):
    print(f"Ok, o que você quer saber sobre {location}?")
    _response_options = input(
        "[T] Temperatura, [V] Ventos, [H] Horário, ou [L] Localização? ")
    if _response_options in "TVHL":
        return _response_options
    return None

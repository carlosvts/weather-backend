def _which_option(option):
    """
    Parse if user wants realtime info(1) or forecast info(2)
    :param str option: input option gived by the user
    """
    current_weather_options = ("1", "realtime")

    forecast_options = ("2", "forecast")

    if option in current_weather_options:
        return "1"

    if option in forecast_options:
        return "2"


def user_input():
    option = input("Welcome to Weather, what do you want to do?"
                   "Realtime [1] or Forecast [2] ?"
                   ).lower().strip()

    possible_options = ("1", "realtime", "forecast", "2")

    if option not in possible_options:
        raise ValueError("Please, enter a valid option")

    return _which_option(option)


def current_weather_localization_input():
    _param = input("Ok! Inform the location: ")
    return _param


def days_input():
    _param = input("Forecast for which day ahead of the current one? ")
    return _param


def weather_response_options(location):
    print(f"Ok, what do you want to know about {location}?")
    _response_options = input(
        "[T] Temperature, [W] Winds, [H] Time, ou [L] Location? "
    ).upper()
    if _response_options in "TVHL":
        return _response_options
    return None


def forecast_response_options(location):
    print(f"Ok, what do you want to know about {location}?")
    _response_options = input(
        "[T] Temperature, [W] Winds or [R] Rain chance? ").upper()
    if _response_options in "TWR":
        return _response_options
    return None

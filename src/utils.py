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
                   "Realtime [1] or Forecast [2]? "
                   ).lower().strip()

    possible_options = ("1", "realtime", "forecast", "2")

    if option not in possible_options:
        raise ValueError("Please, enter a valid option")

    return _which_option(option)


def current_weather_localization_input():
    _param = input("Ok! Inform the location: ")
    return _param


def days_input():
    """
    In the api i chosed, if i pass 1 as a param for the day, it will not show
    the next day, instead it show the current one, so i add this logic of
    adding one to be more "logical" for the user
    """
    _param = input("Forecast for which day ahead of the current one? ")
    try:
        _param = int(_param)
        _param += 1
        return str(_param)
    except ValueError as err:
        print(err, "Please use a number for the day")


def hours_input():
    _param = input("Which hour of this day? ")
    if int(_param) not in range(24):
        raise ValueError("Please, type a hour of the day")
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

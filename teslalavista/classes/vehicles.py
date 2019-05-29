from teslalavista.classes.utilities import Utilities
from teslalavista.classes.api import TeslaAPI
from enum import Enum

class ONLINE_STATE(Enum):
    ASLEEP = 0
    ONLINE = 1

class Charge_State(object):

    def __init__(self, charge_state_json):
        self.battery_heater_on = charge_state_json["battery_heater_on"]
        self.battery_level = charge_state_json["battery_level"]
        self.battery_range = charge_state_json["battery_range"]
        self.charge_current_request = charge_state_json["charge_current_request"]
        self.charge_current_request_max = charge_state_json["charge_current_request_max"]
        self.charge_enable_request = charge_state_json["charge_enable_request"]
        self.charge_energy_added = charge_state_json["charge_energy_added"]
        self.charge_limit_soc = charge_state_json["charge_limit_soc"]
        self.charge_limit_soc_max = charge_state_json["charge_limit_soc_max"]
        self.charge_limit_soc_min = charge_state_json["charge_limit_soc_min"]
        self.charge_limit_soc_std = charge_state_json["charge_limit_soc_std"]
        self.charge_miles_added_ideal = charge_state_json["charge_miles_added_ideal"]
        self.charge_miles_added_rated = charge_state_json["charge_miles_added_rated"]
        self.charge_port_cold_weather_mode = charge_state_json["charge_port_cold_weather_mode"]
        self.charge_port_door_open = charge_state_json["charge_port_door_open"]
        self.charge_port_latch = charge_state_json["charge_port_latch"]
        self.charge_rate = charge_state_json["charge_rate"]
        self.charge_to_max_range = charge_state_json["charge_to_max_range"]
        self.charger_actual_current = charge_state_json["charger_actual_current"]
        self.charger_phases = charge_state_json["charger_phases"]
        self.charger_pilot_current = charge_state_json["charger_pilot_current"]
        self.charger_power = charge_state_json["charger_power"]
        self.charger_voltage = charge_state_json["charger_voltage"]
        self.charging_state = charge_state_json["charging_state"]
        self.conn_charge_cable = charge_state_json["conn_charge_cable"]
        self.est_battery_range = charge_state_json["est_battery_range"]
        self.fast_charger_brand = charge_state_json["fast_charger_brand"]
        self.fast_charger_present = charge_state_json["fast_charger_present"]
        self.fast_charger_type = charge_state_json["fast_charger_type"]
        self.ideal_battery_range = charge_state_json["ideal_battery_range"]
        self.managed_charging_active = charge_state_json["managed_charging_active"]
        self.managed_charging_start_time = charge_state_json["managed_charging_start_time"]
        self.managed_charging_user_canceled = charge_state_json["managed_charging_user_canceled"]
        self.max_range_charge_counter = charge_state_json["max_range_charge_counter"]
        self.not_enough_power_to_heat = charge_state_json["not_enough_power_to_heat"]
        self.scheduled_charging_pending = charge_state_json["scheduled_charging_pending"]
        self.scheduled_charging_start_time = charge_state_json["scheduled_charging_start_time"]
        self.time_to_full_charge = charge_state_json["time_to_full_charge"]
        self.timestamp = charge_state_json["timestamp"]
        self.trip_charging = charge_state_json["trip_charging"]
        self.usable_battery_level = charge_state_json["usable_battery_level"]
        self.user_charge_enable_request = charge_state_json["user_charge_enable_request"]

class Climate_State(object):

    def __init__(self, climate_state_json):
        self.battery_heater = Utilities.set_if_available("battery_heater", climate_state_json)
        self.battery_heater_no_power = Utilities.set_if_available("battery_heater_no_power", climate_state_json)
        self.climate_keeper_mode = Utilities.set_if_available("climate_keeper_mode", climate_state_json)
        self.driver_temp_setting = Utilities.set_if_available("driver_temp_setting", climate_state_json)
        self.fan_status = Utilities.set_if_available("fan_status", climate_state_json)
        self.inside_temp = Utilities.set_if_available("inside_temp", climate_state_json)
        self.is_auto_conditioning_on = Utilities.set_if_available("is_auto_conditioning_on", climate_state_json)
        self.is_climate_on = Utilities.set_if_available("is_climate_on", climate_state_json)
        self.is_front_defroster_on = Utilities.set_if_available("is_front_defroster_on", climate_state_json)
        self.is_preconditioning = Utilities.set_if_available("is_preconditioning", climate_state_json)
        self.is_rear_defroster_on = Utilities.set_if_available("is_rear_defroster_on", climate_state_json)
        self.left_temp_direction = Utilities.set_if_available("left_temp_direction", climate_state_json)
        self.max_avail_temp = Utilities.set_if_available("max_avail_temp", climate_state_json)
        self.min_avail_temp = Utilities.set_if_available("min_avail_temp", climate_state_json)
        self.outside_temp = Utilities.set_if_available("outside_temp", climate_state_json)
        self.passenger_temp_setting = Utilities.set_if_available("passenger_temp_setting", climate_state_json)
        self.remote_heater_control_enabled = Utilities.set_if_available("remote_heater_control_enabled", climate_state_json)
        self.right_temp_direction = Utilities.set_if_available("right_temp_direction", climate_state_json)
        self.seat_heater_left = Utilities.set_if_available("seat_heater_left", climate_state_json)
        self.seat_heater_rear_center = Utilities.set_if_available("seat_heater_rear_center", climate_state_json)
        self.seat_heater_rear_left = Utilities.set_if_available("seat_heater_rear_left", climate_state_json)
        self.seat_heater_rear_left_back = Utilities.set_if_available("seat_heater_rear_left_back", climate_state_json)
        self.seat_heater_rear_right = Utilities.set_if_available("seat_heater_rear_right", climate_state_json)
        self.seat_heater_rear_right_back = Utilities.set_if_available("seat_heater_rear_right_back", climate_state_json)
        self.seat_heater_right = Utilities.set_if_available("seat_heater_right", climate_state_json)
        self.side_mirror_heaters = Utilities.set_if_available("side_mirror_heaters", climate_state_json)
        self.smart_preconditioning = Utilities.set_if_available("smart_preconditioning", climate_state_json)
        self.steering_wheel_heater = Utilities.set_if_available("steering_wheel_heater", climate_state_json)
        self.timestamp = Utilities.set_if_available("timestamp", climate_state_json)
        self.wiper_blade_heater = Utilities.set_if_available("wiper_blade_heater", climate_state_json)

class Drive_State(object):

    def __init__(self, drive_state_json):
        self.gps_as_of = Utilities.set_if_available("gps_as_of", drive_state_json)
        self.heading = Utilities.set_if_available("heading", drive_state_json)
        self.latitude = Utilities.set_if_available("latitude", drive_state_json)
        self.longitude = Utilities.set_if_available("longitude", drive_state_json)
        self.native_latitude = Utilities.set_if_available("native_latitude", drive_state_json)
        self.native_location_supported = Utilities.set_if_available("native_location_supported", drive_state_json)
        self.native_longitude = Utilities.set_if_available("native_longitude", drive_state_json)
        self.native_type = Utilities.set_if_available("native_type", drive_state_json)
        self.power = Utilities.set_if_available("power", drive_state_json)
        self.shift_state = Utilities.set_if_available("shift_state", drive_state_json)
        self.speed = Utilities.set_if_available("speed", drive_state_json)
        self.timestamp = Utilities.set_if_available("timestamp", drive_state_json)

class GUI_State(object):

    def __init__(self, gui_state_json):
        self.gui_24_hour_time = Utilities.set_if_available("gui_24_hour_time", gui_state_json)
        self.gui_charge_rate_units = Utilities.set_if_available("gui_charge_rate_units", gui_state_json)
        self.gui_distance_units = Utilities.set_if_available("gui_distance_units", gui_state_json)
        self.gui_range_display = Utilities.set_if_available("gui_range_display", gui_state_json)
        self.gui_temperature_units = Utilities.set_if_available("gui_temperature_units", gui_state_json)
        self.timestamp = Utilities.set_if_available("timestamp", gui_state_json)

class Vehicle_State(object):
    # TODO: Add speed_limit_mode Class
    def __init__(self, vehicle_state_json):
        self.api_version = Utilities.set_if_available("api_version", vehicle_state_json)
        self.autopark_state_v2 = Utilities.set_if_available("autopark_state_v2", vehicle_state_json)
        self.autopark_style = Utilities.set_if_available("autopark_style", vehicle_state_json)
        self.calendar_supported = Utilities.set_if_available("calendar_supported", vehicle_state_json)
        self.car_version = Utilities.set_if_available("car_version", vehicle_state_json)
        self.center_display_state = Utilities.set_if_available("center_display_state", vehicle_state_json)
        self.df = Utilities.set_if_available("df", vehicle_state_json)
        self.dr = Utilities.set_if_available("dr", vehicle_state_json)
        self.ft = Utilities.set_if_available("ft", vehicle_state_json)
        self.homelink_nearby = Utilities.set_if_available("homelink_nearby", vehicle_state_json)
        self.is_user_present = Utilities.set_if_available("is_user_present", vehicle_state_json)
        self.last_autopark_error = Utilities.set_if_available("last_autopark_error", vehicle_state_json)
        self.locked = Utilities.set_if_available("locked", vehicle_state_json)
        self.media_state = Utilities.set_if_available("media_state", vehicle_state_json)
        self.notifications_supported = Utilities.set_if_available("notifications_supported", vehicle_state_json)
        self.odometer = Utilities.set_if_available("odometer", vehicle_state_json)
        self.parsed_calendar_supported = Utilities.set_if_available("parsed_calendar_supported", vehicle_state_json)
        self.pf = Utilities.set_if_available("pf", vehicle_state_json)
        self.pr = Utilities.set_if_available("pr", vehicle_state_json)
        self.remote_start = Utilities.set_if_available("remote_start", vehicle_state_json)
        self.remote_start_enabled = Utilities.set_if_available("remote_start_enabled", vehicle_state_json)
        self.remote_start_supported = Utilities.set_if_available("remote_start_supported", vehicle_state_json)
        self.rt = Utilities.set_if_available("rt", vehicle_state_json)
        self.sentry_mode = Utilities.set_if_available("sentry_mode", vehicle_state_json)
        self.software_update = Utilities.set_if_available("software_update", vehicle_state_json)
        self.sun_roof_percent_open = Utilities.set_if_available("sun_roof_percent_open", vehicle_state_json)
        self.sun_roof_state = Utilities.set_if_available("sun_roof_state", vehicle_state_json)
        self.timestamp = Utilities.set_if_available("timestamp", vehicle_state_json)
        self.valet_mode = Utilities.set_if_available("valet_mode", vehicle_state_json)
        self.valet_pin_needed = Utilities.set_if_available("valet_pin_needed", vehicle_state_json)
        self.vehicle_name = Utilities.set_if_available("vehicle_name", vehicle_state_json)

class Vehicle_Config(object):

    def __init__(self, vehicle_config_json):
        self.can_accept_navigation_requests = Utilities.set_if_available("can_accept_navigation_requests", vehicle_config_json)
        self.can_actuate_trunks = Utilities.set_if_available("can_actuate_trunks", vehicle_config_json)
        self.car_special_type = Utilities.set_if_available("car_special_type", vehicle_config_json)
        self.car_type = Utilities.set_if_available("car_type", vehicle_config_json)
        self.charge_port_type = Utilities.set_if_available("charge_port_type", vehicle_config_json)
        self.eu_vehicle = Utilities.set_if_available("eu_vehicle", vehicle_config_json)
        self.exterior_color = Utilities.set_if_available("exterior_color", vehicle_config_json)
        self.has_air_suspension = Utilities.set_if_available("has_air_suspension", vehicle_config_json)
        self.has_ludicrous_mode = Utilities.set_if_available("has_ludicrous_mode", vehicle_config_json)
        self.key_version = Utilities.set_if_available("key_version", vehicle_config_json)
        self.motorized_charge_port = Utilities.set_if_available("motorized_charge_port", vehicle_config_json)
        self.perf_config = Utilities.set_if_available("perf_config", vehicle_config_json)
        self.plg = Utilities.set_if_available("plg", vehicle_config_json)
        self.rear_seat_heaters = Utilities.set_if_available("rear_seat_heaters", vehicle_config_json)
        self.rear_seat_type = Utilities.set_if_available("rear_seat_type", vehicle_config_json)
        self.rhd = Utilities.set_if_available("rhd", vehicle_config_json)
        self.roof_color = Utilities.set_if_available("roof_color", vehicle_config_json)
        self.seat_type = Utilities.set_if_available("seat_type", vehicle_config_json)
        self.spoiler_type = Utilities.set_if_available("spoiler_type", vehicle_config_json)
        self.sun_roof_installed = Utilities.set_if_available("sun_roof_installed", vehicle_config_json)
        self.third_row_seats = Utilities.set_if_available("third_row_seats", vehicle_config_json)
        self.timestamp = Utilities.set_if_available("timestamp", vehicle_config_json)
        self.trim_badging = Utilities.set_if_available("trim_badging", vehicle_config_json)
        self.wheel_type = Utilities.set_if_available("wheel_type", vehicle_config_json)

class Vehicle(object):

    def __init__(self, api_object: TeslaAPI, vehicle_json: dict):
        self.api = api_object

        self.id = int(vehicle_json["id"])
        self.name = vehicle_json["display_name"]
        self.option_codes = vehicle_json["option_codes"]
        self.online_state = ONLINE_STATE[vehicle_json["state"].upper()]

        self.config = None
        self.state = None
        self.gui = None
        self.drive = None
        self.climate = None
        self.charge = None

    def update(self) -> None:

        if self.online_state == ONLINE_STATE.ASLEEP:
            self.wake_up()

        details = self.api.vehicle_data(vehicle_id=self.id)

        # details = details.json()["response"]

        self.config = Vehicle_Config(vehicle_config_json=details["vehicle_config"])
        self.state = Vehicle_State(vehicle_state_json=details["vehicle_state"])
        self.gui = GUI_State(gui_state_json=details["gui_settings"])
        self.drive = Drive_State(drive_state_json=details["drive_state"])
        self.climate = Climate_State(climate_state_json=details["climate_state"])
        self.charge = Charge_State(charge_state_json=details["charge_state"])

    def __str__(self) -> str:
        obj_str = "{name} - {id} - {state}".format(
            name=self.name,
            id=self.id,
            state=self.online_state.name
        )

        return obj_str

    '''
        Commands
    '''
    def wake_up(self) -> bool:
        self.api.wake_up(vehicle_id=self.id)

        return True

    def honk_horn(self) -> bool:
        self.api.honk_horn(vehicle_id=self.id)

        return True

    def flash_lights(self) -> bool:
        self.api.flash_lights(vehicle_id=self.id)

        return True

    def remote_start_drive(self, password: str) -> bool:
        self.api.remote_start_drive(vehicle_id=self.id, password=password)

        return True

    # TODO: Connect all remaining commands to API Calls
    def speed_limit_set_limit(self, limit_mph: int) -> bool:
        pass

    def speed_limit_activate(self, pin: int) -> bool:
        pass

    def speed_limit_deactivate(self, pin: int) -> bool:
        pass

    def speed_limit_clear_pin(self, pin: int) -> bool:
        pass

    def set_valet_mode(self, on: bool, password: str) -> bool:
        pass

    def reset_valet_pin(self) -> bool:
        pass

    def set_sentry_mode(self, on: bool) -> bool:
        pass

    def open_trunk(self) -> bool:
        pass

    def open_frunk(self) -> bool:
        pass

    def door_unlock(self) -> bool:
        pass

    def door_lock(self) -> bool:
        pass

    def sunroof_vent(self) -> bool:
        pass

    def sunroof_close(self) -> bool:
        pass

    def charge_port_door_open(self) -> bool:
        pass

    def charge_port_door_close(self) -> bool:
        pass

    def charge_start(self) -> bool:
        pass

    def charge_stop(self) -> bool:
        pass

    def charge_standard(self) -> bool:
        pass

    def charge_max_range(self) -> bool:
        pass

    def set_charge_limit(self, percent: int) -> bool:
        pass

    def auto_conditioning_start(self) -> bool:
        pass

    def auto_conditioning_stop(self) -> bool:
        pass

    def set_temps(self, driver_temp: float, passenger_temp: float) -> bool:
        pass

    def remote_seat_heater_request(self, seat: int, heat_level: int) -> bool:
        pass

    def remote_steering_wheel_heater_request(self, on: bool) -> bool:
        pass

    def media_toggle_playback(self) -> bool:
        pass

    def media_next_track(self) -> bool:
        pass

    def media_prev_track(self) -> bool:
        pass

    def media_next_fav(self) -> bool:
        pass

    def media_prev_fav(self) -> bool:
        pass

    def media_volume_up(self) -> bool:
        pass

    def media_volume_down(self) -> bool:
        pass

    def navigation_request(self, locale: str, address: str) -> bool:
        pass

    def schedule_software_update(self, timestamp: int) -> bool:
        pass

    def cancel_software_update(self) -> bool:
        pass


class VehicleCollection(object):

    def __init__(self):
        self.vehicles = []

    def get_vehicles(self) -> list:
        return self.vehicles

    def get_vehicle_by_name(self, name: str) -> Vehicle:

        for vehicle in self.vehicles:
            if name == vehicle.name:
                return vehicle

    def get_vehicle_by_id(self, id: int) -> Vehicle:

        for vehicle in self.vehicles:
            if id == vehicle.id:
                return vehicle

    def add_vehicle(self, vehicle: Vehicle) -> None:
        self.vehicles.append(vehicle)


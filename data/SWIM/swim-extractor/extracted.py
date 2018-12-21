from pprint import pformat
from typing import Optional, Tuple

from pyxb.binding.datatypes import dateTime


class Extracted_FDPS:
    # should be in everything
    '''
    source: str
    aircraft_id: str
    center: str
    system: str
    timestamp: dateTime
    actual_time: dateTime

    # should be but aren't actually in everything
    arrival_point: Optional[str]
    departure_point: Optional[str]

    # could be in some of them
    aircraft_type: Optional[object]
    route_waypoints: Optional[object]
    route_waypoints_and_timestamps: Optional[object]
    position: Optional[Tuple[float, float]]
    target_position: Optional[Tuple[float, float]]
    altitude: Optional[float]
    target_altitude: Optional[float]
    assigned_altitude: Optional[float]
    speed: Optional[float]
    velocity: Optional[Tuple[float, float]]
    '''
    def __init__(self,
                 source,
                 aircraft_id,
                 center,
                 system,
                 timestamp,
                 actual_time,
                 arrival_point=None,
                 departure_point=None,
                 # could be in some of them
                 aircraft_type=None,
                 route_waypoints=None,
                 route_waypoints_and_timestamps=None,
                 position=None,
                 target_position=None,
                 altitude=None,
                 target_altitude=None,
                 assigned_altitude=None,
                 speed=None,
                 velocity=None):
        self.source = source
        self.aircraft_id = aircraft_id
        self.center = center
        self.system = system
        self.timestamp = timestamp
        self.actual_time = actual_time

        self.arrival_point = arrival_point
        self.departure_point = departure_point

        self.aircraft_type = aircraft_type
        self.route_waypoints = route_waypoints
        self.route_waypoints_and_timestamps = route_waypoints_and_timestamps
        self.position = position
        self.target_position = target_position
        self.altitude = altitude
        self.target_altitude = target_altitude
        self.assigned_altitude = assigned_altitude
        self.speed = speed
        self.velocity = velocity

    def __str__(self):
        """
        Provide human-readable JSON for printing.
        """
        return pformat(vars(self))


class Extracted_SMES:
    '''
    callsign: str
    track: int
    stid: int
    time: dateTime
    event: str
    position: Tuple[float, float]
    altitude: float
    status: str
    '''
    def __init__(self,
                callsign,
                track,
                stid,
                time,
                event,
                position,
                altitude,
                status):
        self.callsign = callsign
        self.track = track
        self.stid = stid
        self.time = time
        self.event = event
        self.position = position
        self.altitude = altitude
        self.status = status

    def __str__(self):
        """
        Provide human-readable JSON for printing.
        """
        return pformat(vars(self))


class Extracted_ASDEX:
    '''
    airport: str
    track: int
    time: dateTime
    is_position_report: bool
    stid: Optional[int]
    position: Optional[tuple]
    '''
    def __init__(self,
                airport,
                track,
                time,
                is_position_report,
                stid=None,
                position=None):
        self.airport = airport
        self.track = track
        self.time = time
        self.is_position_report = is_position_report
        self.stid = stid
        self.position = position

    def __str__(self):
        """
        Provide human-readable JSON for printing.
        """
        return pformat(vars(self))

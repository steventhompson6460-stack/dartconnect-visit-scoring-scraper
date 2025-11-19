import logging
from crawler.match_center_client import MatchCenterClient
from crawler.darts_parser import DartsParser
from crawler.utils_format import load_text_lines

class HistoricalLoader:
 def __init__(self, settings: dict):
 self.client = MatchCenterClient(settings["base_url"])
 self.events_file = settings["events_file"]

 def run(self) -> list:
 all_events = load_text_lines(self.events_file)
 output = []

 for event_id in all_events:
 logging.info(f"Fetching event {event_id} ...")
 match_ids = self.client.fetch_event_matches(event_id)

 for match_id in match_ids:
 match_payload = self.client.fetch_match(match_id)
 parsed = DartsParser.parse_match_payload(match_id, event_id, match_payload)
 output.extend(parsed)

 return output
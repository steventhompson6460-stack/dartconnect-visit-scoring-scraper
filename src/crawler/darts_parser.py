import logging

class DartsParser:
 @staticmethod
 def parse_match_payload(match_id: str, event_id: str, payload: dict) -> list:
 results = []

 legs = payload.get("legs", [])
 for leg_index, leg in enumerate(legs, start=1):
 visits = leg.get("visits", [])

 for i, visit in enumerate(visits, start=1):
 try:
 entry = {
 "match_id": match_id,
 "event_id": event_id,
 "player_name": visit.get("player", "Unknown"),
 "visit_index": i,
 "score": visit.get("score", 0),
 "dart_count": visit.get("darts", 3),
 "leg_number": leg_index,
 "set_number": visit.get("set", 1),
 "timestamp": payload.get("timestamp"),
 "raw_payload": visit,
 }
 results.append(entry)
 except Exception as e:
 logging.error(f"Parsing error on match {match_id}: {e}")

 return results
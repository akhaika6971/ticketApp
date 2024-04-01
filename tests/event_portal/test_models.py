from event_portal.models import *
from tests.utils.setup import TestSetup
from event_portal.api.serializers import EventSerializer

class EventModelTestCase(TestSetup):
    
    def setUp(self) -> None:
        event_serializer = EventSerializer(data={
            "title": "Bridging the gap between Finance and Technology",
            "event_start_date": "2024-10-30",
            "event_start_time": "12:00:00",
            "event_end_date": "2024-11-01",
            "event_end_time": "06:00:00",
            "location": "Nairobi",
            "address": "8, Kaburu Drive, Pine Tree, Kilimani",
            "category": [
                "Technology"
            ],
            "about": "A tech event"
        })
        event_serializer.is_valid(raise_exception=True)
        self.event = event_serializer.save(host=self.create_test_superuser())
        return super().setUp()
    
    def test_event_model(self):
        self.assertTrue(isinstance(self.event, Event))
        self.assertTrue(self.event.host.event_hoster)
        

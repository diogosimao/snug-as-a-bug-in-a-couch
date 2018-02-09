from django.test import TestCase

from apps.list_manager.models import WatchList


class WatchListModelTestCase(TestCase):

    def setUp(self):
        self.old_count = WatchList.objects.count()
        self.item = WatchList(tmdb_id=1)
        self.item.save()

    def test__model_can_create_item(self):
        self.assertNotEqual(self.old_count, WatchList.objects.count())
        self.assertTrue(isinstance(self.item, WatchList))

    def test__model_can_return_item_id(self):
        self.assertEqual(self.item.__str__(), 1)

    def test__model_can_update_item(self):
        self.item.seen = True
        self.item.save()
        self.assertTrue(WatchList.objects.first().seen)

    def test__model_can_delete_item(self):
        WatchList.objects.all().delete()
        self.assertEqual(WatchList.objects.count(), 0)

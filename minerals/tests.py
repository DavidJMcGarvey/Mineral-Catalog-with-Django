from django.urls import reverse

from django.test import TestCase

from .models import Mineral


class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name="",
            image_filename="",
            image_caption="",
            category="",
            formula="",
            strunz_classification="",
            color="",
            crystal_system="",
            unit_cell="",
            crystal="",
            symmetry="",
            cleavage="",
            mohs_scale_hardness="",
            luster="",
            streak="",
            diaphaneity="",
            optical_properties="",
            refractive_index="",
            crystal_habit="",
            specific_gravity="",
        )

    def test_minerals_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/minerals_list.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])

    def test_mineral_random_view(self):
        resp = self.client.get(reverse('minerals:random'))
        self.assertEqual(resp.status_code, 200)
        self.assertNotEqual(self.mineral.name, resp.context['mineral'])


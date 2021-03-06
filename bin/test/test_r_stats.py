from test_service import Service
from test_path import PathTestCase
import r_stats
import r_packages
import r_index_logging


class RStatsTestCase(PathTestCase):
    def test_get_r_config_file(self):
        r_index_logging.clear_log_entries()

        service = Service()
        r_packages.add(service,'boot')
        r_stats.r_stats(service)
        indexed_events = r_index_logging.get_log_entries()

        self.assertEqual(len(indexed_events), 2)

        self.assertTrue('stats_package_name=\"boot\"' in indexed_events[0])

        self.assertTrue('stats_number_of_packages=\"1\"' in indexed_events[1])
from test_service import Service, Stanza
from test_path import PathTestCase
import os
import r_scripts
import time


class ScriptsTestCase(PathTestCase):
    def test_update_library(self):
        service = Service([
            Stanza('script://test', {
                'content': 'YWRkIDwtIGZ1bmN0aW9uKGEsYikgew0KICBjID0gYStiDQogIHJldHVybihjKQ0KfQ0KcmVzdWx0ID0gY'
                           'WRkKDQsMjAwKQ0Kb3V0cHV0ID0gZGF0YS5mcmFtZShSZXN1bHQ9YyhyZXN1bHQpKQ==',
            }),
        ])
        r_scripts.create_files(service)
        installed_scripts = os.listdir(r_scripts.get_custom_scripts_path())
        self.assertEqual(len(installed_scripts), 1)
        self.assertEqual(installed_scripts[0], 'test.r')

        mtime = os.path.getmtime(os.path.join(r_scripts.get_custom_scripts_path(), installed_scripts[0]))
        r_scripts.create_files(service)
        self.assertEqual(
            mtime,
            os.path.getmtime(os.path.join(r_scripts.get_custom_scripts_path(), installed_scripts[0]))
        )

        time.sleep(1.5)
        r_scripts.add(service, 'test', """
add <- function(a,b) {
  c = a+b
  return(c)
}
result = add(4,10)
output = data.frame(Result=c(result))
        """)
        time.sleep(1.5)
        r_scripts.create_files(service)
        installed_scripts = os.listdir(r_scripts.get_custom_scripts_path())
        self.assertEqual(len(installed_scripts), 1)
        self.assertEqual(installed_scripts[0], 'test.r')

        self.assertNotEqual(
            mtime,
            os.path.getmtime(os.path.join(r_scripts.get_custom_scripts_path(), installed_scripts[0]))
        )
        mtime = os.path.getmtime(os.path.join(r_scripts.get_custom_scripts_path(), installed_scripts[0]))
        r_scripts.create_files(service)
        self.assertEqual(
            mtime,
            os.path.getmtime(os.path.join(r_scripts.get_custom_scripts_path(), installed_scripts[0]))
        )
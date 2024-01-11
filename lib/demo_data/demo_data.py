import sys

from lib.demo_data.pokemon import add_pokemon
from lib.demo_data.shiny_pokemon import add_shiny_pokemon
# from lib.demo_data.tags import tags
# from lib.demo_data.users import add_users
# from lib.demo_data.organizations import add_orgs
# from lib.demo_data.record_type import record_types
# from lib.demo_data.tags_ob_xref import tag_obj_xref
# from lib.demo_data.custom_fields import custom_fields
# from lib.demo_data.roles_permissions import org_role_permissions
# from lib.demo_data.custom_field_values import custom_field_values
# from lib.demo_data.custom_field_options import custom_field_options
# from lib.demo_data.record_type_custom_fields_xref import record_xref


def run_demo_data():
    if len(sys.argv) > 1 and sys.argv[1] == 'demo-data':
        print("Creating Demo Data...")

        add_pokemon()
        add_shiny_pokemon()
        # org_role_permissions()
        # add_users()
        # tags()
        # tag_obj_xref()
        # record_types()
        # custom_fields()
        # custom_field_values()
        # custom_field_options()
        # record_xref()
# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_create_grocery_item 1'] = {
    'data': {
        'createGroceryItem': {
            'groceryItem': {
                'id': 'R3JvY2VyeUl0ZW1PYmplY3Q6MQ==',
                'isDone': False,
                'label': 'Celery'
            }
        }
    }
}

snapshots['test_delete_grocery_item 1'] = {
    'data': {
        'deleteGroceryItem': {
            'ok': True
        }
    }
}

snapshots['test_modify_grocery_item 1'] = {
    'data': {
        'modifyGroceryItem': {
            'groceryItem': {
                'id': 'R3JvY2VyeUl0ZW1PYmplY3Q6MQ==',
                'isDone': False,
                'label': 'Onions'
            }
        }
    }
}

snapshots['test_modify_grocery_item 2'] = {
    'data': {
        'modifyGroceryItem': {
            'groceryItem': {
                'id': 'R3JvY2VyeUl0ZW1PYmplY3Q6MQ==',
                'isDone': True,
                'label': 'Onions'
            }
        }
    }
}

snapshots['test_query_all_grocery_items 1'] = {
    'data': {
        'allGroceryItems': {
            'edges': [
                {
                    'node': {
                        'id': 'R3JvY2VyeUl0ZW1PYmplY3Q6MQ==',
                        'isDone': False,
                        'label': 'Celery'
                    }
                },
                {
                    'node': {
                        'id': 'R3JvY2VyeUl0ZW1PYmplY3Q6Mg==',
                        'isDone': False,
                        'label': 'Peppers'
                    }
                }
            ]
        }
    }
}

snapshots['test_query_grocery_item 1'] = {
    'data': {
        'groceryItem': {
            'isDone': False,
            'label': 'Celery'
        }
    }
}

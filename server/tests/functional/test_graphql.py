mutations = {
  'create_grocery_item': '''
    mutation CreateGroceryItem ($label: String!){
      createGroceryItem(label: $label) {
        groceryItem {
          id,
          label,
          isDone
        }
      }
    }
  ''',
  
  'delete_grocery_item': '''
    mutation deleteGroceryItem ($deleteGroceryItemInput: DeleteGroceryItemInput!) {
      deleteGroceryItem(input:$deleteGroceryItemInput) {
        ok
      }
    }
  '''
}
queries = {
  'all_grocery_items': '''
    query allGroceryItems {
      allGroceryItems {
        edges {
          node {
            id,
            label,
            isDone
          }
        }
      }
    }
  ''',

  'grocery_item': '''
    query groceryItem ($id: ID!) {
      groceryItem(id:$id) {
        label,
        isDone
      }
    }
  '''
}

def test_create_grocery_item(session, graphene_client, snapshot):
  variables = {
    "label": "Celery"
  }
  snapshot.assert_match(graphene_client.execute(mutations['create_grocery_item'], variables=variables))

def test_delete_grocery_item(session, graphene_client, snapshot):
  variables = {
    "label": "Celery", 
    "deleteGroceryItemInput": {
      "id": "R3JvY2VyeUl0ZW1PYmplY3Q6MQ=="
    }
  }
  graphene_client.execute(mutations['create_grocery_item'], variables=variables)
  snapshot.assert_match(graphene_client.execute(mutations['delete_grocery_item'], variables=variables))

def test_query_all_grocery_items(session, graphene_client, snapshot):
  variables = {
    "label": "Celery"
  }
  graphene_client.execute(mutations['create_grocery_item'], variables=variables)
  variables = {
    "label": "Peppers"
  }
  graphene_client.execute(mutations['create_grocery_item'], variables=variables)
  snapshot.assert_match(graphene_client.execute(queries['all_grocery_items']))

def test_query_grocery_item(session, graphene_client, snapshot):
  variables = {
    "label": "Celery",
    "id": "R3JvY2VyeUl0ZW1PYmplY3Q6MQ=="
  }
  graphene_client.execute(mutations['create_grocery_item'], variables=variables)
  snapshot.assert_match(graphene_client.execute(queries['grocery_item'], variables=variables))
entities = [
    {
        'entity'     : 1,
        'username'   : 'admin',
        'email'      : 'admin@intellichef.com',
        'password'   : '5CC',
        'first_name' : 'Intelli',
        'last_name'  : 'Chef',
        'logged_in'  : 'True',
        'allergies'  : [],
        'dietary_concerns' : []
    },
    {
        'entity'     : 2,
        'username'   : 'user',
        'email'      : 'user@intellichef.com',
        'password'   : '5CC',
        'first_name' : 'Zach',
        'last_name'  : 'Bubble',
        'logged_in'  : 'True',
        'allergies'  : [],
        'dietary_concerns' : []
    }
]

recipes = [
    {
        'recipe':1,
        'name': 'Linguine',
        'instructions': 'Example Instructions',
        'description': 'Example Description',
        'url': 'http://www.allrecipes.com/',
        'is_calibration_recipe': True,
        'rating': 3.5
    },
    {
        'recipe':2,
        'name': 'Macaroni',
        'instructions': 'Example Instructions',
        'description': 'Example Description',
        'is_calibration_recipe': False,
        'url': 'http://www.allrecipes.com/',
        'rating': 4
    }
]

meal_plans = {
    '3-1-2017': {
        'breakfast': recipes[0],
        'lunch': recipes[0],
        'dinner': recipes[0]
    },
    '3-2-2017': {
        'breakfast': recipes[0],
        'lunch': recipes[0],
        'dinner': recipes[0]
    },
    '3-3-2017': {
        'breakfast': recipes[0],
        'lunch': recipes[0],
        'dinner': recipes[0]
    },
    '3-4-2017': {
        'breakfast': recipes[0],
        'lunch': recipes[0],
        'dinner': recipes[0]
    },
    '3-5-2017': {
        'breakfast': recipes[0],
        'lunch': recipes[0],
        'dinner': recipes[0]
    },
    '3-6-2017': {
        'breakfast': recipes[0],
        'lunch': recipes[0],
        'dinner': recipes[0]
    },
    '3-7-2017': {
        'breakfast': recipes[0],
        'lunch': recipes[0],
        'dinner': recipes[0]
    }
}

def get_recipes():
    return recipes

def get_calibration_recipes():
    return filter(lambda r: r['is_calibration_recipe'] == True, recipes)

def get_most_popular_recipes():
    return sorted(recipes, cmp=lambda y, x: int(round(x['rating'] - y['rating'])))

def create_or_update_recipe_rating( recipe_rating ):
    return recipe_rating

def create_entity(new_entity):
    last_entity = max(entities, key=lambda e: e['entity'])
    new_entity['entity'] = last_entity['entity'] + 1
    new_entity['logged_in'] = True
    entities.append(new_entity)

    return new_entity

def get_meal_plan(date):
    if( date not in meal_plans ):
        return None
    return meal_plans[date]

def get_entity( entity_identifier ):
    entity = filter(
        lambda e: e['email'] == entity_identifier or e['username'] == entity_identifier or e['entity'] == entity_identifier,
        entities
    )

    if len(entity) == 0:
        return False
    if len(entity) > 1:
        return None

    return entity[0]

def delete_entity(entity_pk):
    for i in xrange(len(entities)):
        if(entities[i]['entity'] == entity_pk):
            del entities[i]
            return True

    return False

def update_entity( entity_pk, updated_entity ):
    entity = filter(lambda e: e['entity'] == entity_pk, entities)

    if len(entity) != 1:
        return None

    entity = entity[0]
    if( 'email' in updated_entity and updated_entity['email'] is not None ):
        entity['email'] = updated_entity['email']

    if( 'password' in updated_entity and updated_entity['password'] is not None ):
        entity['password'] = updated_entity['password']

    if( 'first_name' in updated_entity and updated_entity['first_name'] is not None ):
        entity['first_name'] = updated_entity['first_name']

    if( 'last_name' in updated_entity and updated_entity['last_name'] is not None ):
        entity['last_name'] = updated_entity['last_name']

    if( 'allergies' in updated_entity and updated_entity['allergies'] is not None ):
        entity['allergies'] = updated_entity['allergies']

    if( 'dietary_concerns' in updated_entity and updated_entity['dietary_concerns'] is not None ):
        entity['dietary_concerns'] = updated_entity['dietary_concerns']

    return entity



from django.test import TestCase
from rest_framework.test import APIClient


class TestAnimalView(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.animal_data = {
            "name": "amora",
            "age": 5,
            "weight": 30,
            "sex": "female",
            "group": {"name": "cão", "scientific_name": "canis familiaris"},
            "characteristics": [
                {"name": "peludo"},
                {"name": "medio porte"},
            ],
        }

        self.animal_data_2 = {
            "name": "hanna",
            "age": 1,
            "weight": 20,
            "sex": "female",
            "group": {"name": "gato", "scientific_name": "felis catus"},
            "characteristics": [
                {"name": "peludo"},
                {"name": "pequeno porte"},
            ],
        }

        self.animal_data_3 = {
            "name": "zé",
            "age": 15,
            "weight": 10,
            "sex": "male",
            "group": {"name": "papagaio", "scientific_name": "amazona"},
            "characteristics": [
                {"name": "com penas"},
                {"name": "com bico"},
            ],
        }

        self.animal_data_4 = {
            "name": "amora",
            "age": 5,
            "weight": 30,
            "sex": "female",
            "group": {"name": "cão", "scientific_name": "canis familiaris"},
            "characteristics": [
                {"name": "peludo"},
                {"name": "medio porte"},
            ],
        }
    
    def test_create_animal(self):
        output_data = {
            "id": 1,
            "name": "amora",
            "age": 5,
            "weight": 30,
            "sex": "female",
            "group": {"id": 1, "name": "cão", "scientific_name": "canis familiaris"},
            "characteristics": [
                {"id": 1, "name": "peludo"},
                {"id": 2, "name": "medio porte"},
            ],
        }

        # create animal
        post_response = self.client.post(
            "/api/animals/", self.animal_data, format="json"
        )
        self.assertDictContainsSubset({"id": 1}, post_response.json())
        self.assertDictContainsSubset(output_data, post_response.json())
        self.assertEqual(post_response.status_code, 201)
        
    def test_list_animals(self):
        # testa se retorna lista vazia, request GET sem nenhum animal cadastrado
        get_response = self.client.get("/api/animals/", format="json")
        self.assertEqual(get_response.json(), [])
        self.assertEqual(get_response.status_code, 200)

        # testa se o request GET retorna 3 objetos
        self.client.post("/api/animals/", self.animal_data, format="json")
        self.client.post("/api/animals/", self.animal_data_2, format="json")
        self.client.post("/api/animals/", self.animal_data_3, format="json")
        get_response_all = self.client.get("/api/animals/", format="json")

        self.assertEqual(len(get_response_all.json()), 3)
        self.assertEqual(get_response.status_code, 200)
        
    def test_get_two_animals_alike(self):
        # testa se dois animais iguais quando adicionados geram id's distintos
        self.client.post("/api/animals/", self.animal_data, format="json")
        self.client.post("/api/animals/", self.animal_data_4, format="json")
        get_response = self.client.get("/api/animals/", format="json")

        # testa se realmente retornou 2 animais
        self.assertEqual(len(get_response.json()), 2)

        first_id = get_response.json()[0]['id']
        second_id = get_response.json()[1]['id']

        # testa se os dois id's retornados são diferentes
        self.assertNotEqual(first_id, second_id)

    def test_filter_animals(self):
        # testa a response quando tentamos filtrar sem nenhum animal cadastrado
        get_response = self.client.get("/api/animals/1/", format="json")
        self.assertEqual(get_response.status_code, 404)

        # testa o retorno após um animal ser cadastrado
        self.client.post("/api/animals/", self.animal_data, format="json")
        get_response = self.client.get("/api/animals/1/", format="json")
        self.assertEqual(get_response.status_code, 200)
        self.assertDictContainsSubset({"id": 1}, get_response.json())
    
    def test_delete_animal(self):
        # testa se após buscar o animal deletado, ele tem o retorno esperado
        self.client.post("/api/animals/", self.animal_data, format="json")
        delete_response = self.client.delete("/api/animals/1/", format="json")
        delete_response_2 = self.client.delete("/api/animals/1/", format="json")
        self.assertEqual(delete_response.status_code, 204)
        self.assertEqual(delete_response_2.status_code, 404)
    
    def test_create_two_animals_with_the_same_characteristic(self):
        # testa se o id da caracteristica "peludo" é o mesmo para ambos os requests
        post_response = self.client.post(
            "/api/animals/", self.animal_data, format="json"
        )
        
        post_response_2 = self.client.post(
            "/api/animals/", self.animal_data_2, format="json"
        )

        first_id_peludo = [
            char["id"] for char in post_response.json()["characteristics"] if char["name"] == "peludo"
            ]
        second_id_peludo = [
            char["id"] for char in post_response_2.json()["characteristics"] if char["name"] == "peludo"
            ]
        
        self.assertEqual(first_id_peludo, second_id_peludo)
        self.assertEqual(post_response_2.status_code, 201)
    
    def test_create_two_animals_with_the_same_group(self):
        # testa se o mesmo grupo não foi criado duas vezes
        post_response = self.client.post(
            "/api/animals/", self.animal_data, format="json"
        )
        
        post_response_3 = self.client.post(
            "/api/animals/", self.animal_data_4, format="json"
        )
        self.assertDictEqual(
            post_response.json()["group"], post_response_3.json()["group"]
        )
        self.assertEqual(post_response_3.status_code, 201)

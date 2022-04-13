from unittest import TestCase, main

from custom_hashmap import HashTable


class TestHashTable(TestCase):
    def test_init(self):
        table = HashTable()
        self.assertEqual([None, None, None, None], table._HashTable__keys)
        self.assertEqual([None, None, None, None], table._HashTable__values)
        self.assertEqual(4, table.max_capacity)

    def test_get_item_dunder(self):
        table = HashTable()
        table["name"] = "Test"
        table["age"] = 0
        result = table["name"]
        self.assertEqual("Test", result)

    def test_get_item_dunder_non_existing_key_raises(self):
        table = HashTable()
        table["name"] = "Test"
        table = HashTable()
        table["name"] = "Test"
        with self.assertRaises(KeyError) as ex:
            # Non-existing key
            table["sssa"]
        self.assertEqual("sssa", str(ex.exception.args[0]))

    def test_set_item_dunder_replace_value_of_existing_key(self):
        table = HashTable()
        table["name"] = "Test"
        self.assertEqual("Test", table["name"])
        table["name"] = "New Test"
        self.assertEqual("New Test", table["name"])

    def test_table_is_full_set_item_dunder_resizes(self):
        table = HashTable()
        table["name"] = "Peter"
        table["age"] = 45
        table["is_pet_owner"] = True
        table["weight"] = 100
        self.assertEqual(4, table.size())
        self.assertEqual(4, table.max_capacity)
        table["son"] = "Chris"
        self.assertEqual(5, table.size())
        self.assertEqual(8, table.max_capacity)

    def test_set_item_collision_linear_approach_is_taken(self):
        table = HashTable()
        table["name"] = "Peter"
        occ_index = table._HashTable__keys.index("name")
        self.assertEqual(1, occ_index)
        expected_index = table._HashTable__calc_index("age")
        # Coll will happen
        self.assertEqual(1, expected_index)
        # Actual index shd be next available one
        table["age"] = 0
        self.assertEqual(2, table._HashTable__keys.index("age"))

    def test_set_item_dunder_linear_approach_starts_at_the_beginning_when_reaches_end(self):
        table = HashTable()
        table["name"] = "Peter"
        table["age"] = 45
        table["is_pet_owner"] = True
        self.assertEqual([None, "name", "age", "is_pet_owner"], table._HashTable__keys)
        table["weight"] = 100
        self.assertEqual(["weight", "name", "age", "is_pet_owner"], table._HashTable__keys)

    def test_size_returns_only_occupied_places_count(self):
        table = HashTable()
        table["name"] = "Peter"
        self.assertEqual(4, table.max_capacity)
        res = table.size()
        self.assertEqual(1, res)
        table["age"] = 45
        res = table.size()
        self.assertEqual(4, table.max_capacity)
        self.assertEqual(2, res)

    def test_add_adds_pair(self):
        table = HashTable()
        self.assertEqual([None, None, None, None], table._HashTable__keys)
        table.add("age", 12)
        self.assertEqual([None, "age", None, None], table._HashTable__keys)

    def test_dunder_str(self):
        table = HashTable()
        table["name"] = "Peter"
        table["age"] = 45
        result = table.__str__()
        expected_res = "{name: Peter, age: 45}"
        self.assertEqual(expected_res, result)

    def test_get_non_existing_key_returns_none(self):
        table = HashTable()
        self.assertEqual([None, None, None, None], table._HashTable__keys)
        res = table.get("somekey")
        self.assertEqual(None, res)

    def test_get_w_default_val(self):
        table = HashTable()
        self.assertEqual([None, None, None, None], table._HashTable__keys)
        res = table.get("somekey", "default val")
        self.assertEqual("default val", res)

    def test_get_existing_key_returns_value(self):
        table = HashTable()
        table["name"] = "Peter"
        res = table.get("name")
        self.assertEqual("Peter", res)

    def test_len_returns_max_capacity(self):
        table = HashTable()
        self.assertEqual(4, table.max_capacity)
        # Does not change length
        table["name"] = "test"
        self.assertEqual(4, table.max_capacity)
        res = len(table)
        self.assertEqual(4, res)


if __name__ == "__main__":
    main()
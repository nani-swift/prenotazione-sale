import unittest
from datetime import date, datetime
from prenotazioni import Prenotazione


class TestPrenotazione(unittest.TestCase):
    def setUp(self) -> None:
        self.giorno = date(2026, 11, 24)

    def test_orari_non_ammessi_sollevano_value_error(self) -> None:
        casi_orari = [
            ("08:15", "09:00"),
            ("07:30", "08:30"),
            ("19:30", "20:30"),
            ("11:00", "11:00"),
            ("12:00", "10:30"),
        ]
        for inizio, fine in casi_orari:
            with self.subTest(inizio=inizio, fine=fine):
                with self.assertRaises(ValueError):
                    Prenotazione("A1",self.giorno,inizio,fine,"ALDO",2,)

    def test_giorno_non_date_solleva_type_error(self) -> None:
        giorni_non_validi = [
            "2026-11-24",
            datetime(2026, 11, 24, 9, 0),
            None,
        ]
        for giorno in giorni_non_validi:
            with self.subTest(giorno=giorno):
                with self.assertRaises(TypeError):
                    Prenotazione("A1",giorno,"09:00","10:00","ANIR",2,)

    def test_durata_minuti_restituisce_durata_corretta(self) -> None:
        prenotazione = Prenotazione("A1",self.giorno,"09:00","10:30","TILILA",3,)

        durata = prenotazione.durata_minuti()

        self.assertEqual(durata, 90)


if __name__ == "__main__":
    unittest.main()
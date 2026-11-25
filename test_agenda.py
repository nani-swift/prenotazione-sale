import unittest
from datetime import date, timedelta
from prenotazioni import (
    Agenda,
    DataNonAmmessa,
    ORIZZONTE_GIORNI,
    Prenotazione,
    PrenotazioneNonTrovata,
    Sala,
    SalaNonTrovata,
)


class TestAgenda(unittest.TestCase):
    def setUp(self) -> None:
        self.agenda = Agenda()
        self.sala = Sala("A1", "Aula 1", 20)
        self.agenda.aggiungi_sala(self.sala)
        self.oggi = date(2026, 11, 20)

    def test_aggiungi_sala_duplicata_e_sala_inesistente(self) -> None:
        with self.assertRaises(ValueError):
            self.agenda.aggiungi_sala(Sala("A1", "Duplicato", 10))

        with self.assertRaises(SalaNonTrovata):
            self.agenda.sala("INESISTENTE")

    def test_prenota_regole_data_e_oggi_ammesso(self) -> None:
        data_passata = self.oggi - timedelta(days=1)
        domenica = date(2026, 11, 22)
        oltre_orizzonte = self.oggi + timedelta(days=ORIZZONTE_GIORNI + 1)

        for data_non_ammessa in (data_passata, domenica, oltre_orizzonte):
            with self.subTest(giorno=data_non_ammessa):
                p = Prenotazione("A1",data_non_ammessa,"09:00","10:00","ALDO",5,)
                with self.assertRaises(DataNonAmmessa):
                    self.agenda.prenota(p, oggi=self.oggi)

        p_oggi = Prenotazione("A1",self.oggi,"09:00","10:00","ANIR",5,)
        id_creato = self.agenda.prenota(p_oggi, oggi=self.oggi)
        self.assertEqual(id_creato, 1)

    def test_cancella_e_prenotazione_id_inesistente(self) -> None:
        with self.assertRaises(PrenotazioneNonTrovata):
            self.agenda.prenotazione(999)

        with self.assertRaises(PrenotazioneNonTrovata):
            self.agenda.cancella(999)


if __name__ == "__main__":
    unittest.main()
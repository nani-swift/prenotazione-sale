import unittest
from datetime import date
from prenotazioni import Agenda, ConflittoOrario, Prenotazione, Sala


class TestSegnalazioni(unittest.TestCase):
    def setUp(self) -> None:
        self.agenda = Agenda()
        self.sala = Sala("A2", "Aula 2", 10)
        self.agenda.aggiungi_sala(self.sala)
        self.giorno = date(2026, 11, 24)
        self.oggi = date(2026, 11, 20)

    def test_prenotazioni_contigue_non_in_conflitto(self) -> None:
        prima = Prenotazione("A2", self.giorno, "09:00", "10:00", "ALDO", 4)
        seconda = Prenotazione("A2", self.giorno, "10:00", "11:00", "ANIR", 5)
        self.agenda.prenota(prima, oggi=self.oggi)

        try:
            id_seconda = self.agenda.prenota(seconda, oggi=self.oggi)
        except ConflittoOrario:
            self.fail("Due prenotazioni contigue non devono sollevare ConflittoOrario")

        self.assertEqual(self.agenda.prenotazione(id_seconda).inizio, "10:00")
        self.assertEqual(self.agenda.prenotazione(id_seconda).fine, "11:00")

    def test_prenotazione_con_capienza_esatta_consentita(self) -> None:
        sala_riunioni = Sala("SR1", "Sala riunioni", 10)
        self.agenda.aggiungi_sala(sala_riunioni)
        prenotazione = Prenotazione("SR1", self.giorno, "14:00", "15:00", "TILILA", 10)

        id_prenotazione = self.agenda.prenota(prenotazione, oggi=self.oggi)

        self.assertEqual(self.agenda.prenotazione(id_prenotazione).partecipanti, 10)

if __name__ == "__main__":
    unittest.main()
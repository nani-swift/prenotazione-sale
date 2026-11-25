import unittest
from datetime import date, time
from prenotazioni import Agenda, Sala


class TestSegnalazioni(unittest.TestCase):
    def setUp(self) -> None:
        self.agenda = Agenda()
        self.sala = Sala(codice="A2", nome="Aula 2", capienza=10)
        self.agenda.aggiungi_sala(self.sala)
        self.giorno = date(2026, 11, 24)
        self.oggi = date(2026, 11, 20)

    def test_prenotazioni_contigue_non_in_conflitto(self) -> None:
        self.agenda.prenota(
            sala_codice="A2",
            giorno=self.giorno,
            inizio=time(9, 0),
            fine=time(10, 0),
            referente="ALDO",
            partecipanti=4,
            oggi=self.oggi,
        )

        prenotazione_successiva = self.agenda.prenota(
            sala_codice="A2",
            giorno=self.giorno,
            inizio=time(10, 0),
            fine=time(11, 0),
            referente="ANIR",
            partecipanti=5,
            oggi=self.oggi,
        )

        self.assertEqual(prenotazione_successiva.inizio, time(10, 0))
        self.assertEqual(prenotazione_successiva.fine, time(11, 0))


if __name__ == "__main__":
    unittest.main()
    
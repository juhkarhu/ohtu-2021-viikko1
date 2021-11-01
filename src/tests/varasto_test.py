import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_varaston_str_toimii_tyhjalla_varastolla(self):
        elf.assertEqual(str(self.varasto), 'saldo = 0, vielä tilaa 10')

    def test_konstruktori_toimii_negatiisivella_tilavuudella(self):
        self.warehouse = Varasto(-2)
        self.assertAlmostEqual(self.warehouse.tilavuus, 0)

    def test_konstruktori_toimii_negatiisivella_saldolla(self):
        self.warehouse = Varasto(10, -2)
        self.assertAlmostEqual(self.warehouse.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_negatiivinen_lisays_ei_vaikuta_saldoon(self):
        self.varasto.lisaa_varastoon(-10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_varaston_lisays_kerralla_tayteen(self):
        self.varasto.lisaa_varastoon(10)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_tavaraa_ei_voi_lisata_enemman_kuin_saldoa_on(self):
        self.varasto.lisaa_varastoon(20)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_varaston_vahennys_negatiivisella_ei_mahdollista(self):
        self.varasto.lisaa_varastoon(2)
        # Varaston saldo nyt 2
        self.varasto.ota_varastosta(-10)
        self.assertAlmostEqual(self.varasto.saldo, 2)

    def test_saldo_ei_mene_negatiivisesi_jos_otetaan_yli_saldon(self):
        self.varasto.lisaa_varastoon(10)
        # Varaston saldo nyt 10
        nostettu_maara = self.varasto.ota_varastosta(20)
        self.assertAlmostEqual(nostettu_maara, 10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

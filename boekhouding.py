from helper import*
from presentatie import*
import csv

inkomsten={
    "Aardbeien-ijs-totaal":1000,
    "Vanille-ijs-totaal":2000,
    "Chocolade-ijs-totaal":1500,
    "Waterijsjes-totaal":750,
}
totale_inkomsten=som(inkomsten)
presenteer(inkomsten,totale_inkomsten)

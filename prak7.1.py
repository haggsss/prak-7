# -*- coding: utf-8 -*-
"""
Created on Sat May 11 08:39:28 2024

@author: kusfi
"""

class Dog:
    def __init__(self, nama, jenis=None, umur=None, warna=None):
        self.nama = nama
        self.jenis = jenis
        self.umur = umur
        self.warna = warna
        
    def set_nama(self, nama):
        self.nama = nama
        
    def set_color(self, warna):
        self.warna = warna
        
    def message(self):
        return (f"Halo, nama saya {self.nama}.\n"
                f"Jenis, Usia, dan Warna saya adalah {self.jenis}, {self.umur}, {self.warna}")
    
if __name__ == "__main__":
    tuffy = Dog("Tuffy", "papillon", 5, "white")
    max = Dog("Max", "Great Dane", 7, "black")
    print(tuffy.message())
    print(max.message())
    
    lala = None
    unknown = Dog("Shih Tzu")
    
    lala = unknown
    lala.set_nama("Lala")
    lala.set_color("brown")
    print(lala.message())

    unknown = tuffy
    unknown.set_nama("Max")
    tuffy = max
    max = unknown
    print(tuffy.message())
    print(max.message())

import hashlib

class BruteForcer:
    def hashing(self, s: str):
        m = hashlib.sha256()

        for _ in range(1):
            m.update(s.encode())
        
        return m.hexdigest()

    def brute_force_list(self, expected_hash, path = None, callback=None):
        l = open(path if path else "password_files/wordlist.txt", "r").readlines()
        for i in range(len(l)):
            if callback:
                word = l[i].replace("\n","")
                callback(f"Modo: Lista\nHash: {expected_hash}\nTentando: {word}\nPosição {i+1}-{len(l)}")
            if self.hashing(word) == expected_hash:
                return word
        return None
    
    def brute_force_range(self, expected_hash, r: str, callback=None):
        range_l = list(map(int, r.split("-")))
        ran = range(*range_l)
        for i in ran:
            if callback:
                callback(f"Modo: Intervalo\nHash: {expected_hash}\nPosição {i+1}-{r.split('-')[1]}")
            if self.hashing(str(i)) == expected_hash:
                return i
        return None
    
    @property
    def modes(self):
        return {"list": self.brute_force_list, "range": self.brute_force_range}

    def force(self, hash_passwd, mode: dict, args, callback=None):
        forcer = self.modes[mode]
        return forcer(hash_passwd, args, callback)

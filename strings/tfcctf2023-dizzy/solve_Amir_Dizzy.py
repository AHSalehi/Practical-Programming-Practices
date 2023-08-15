def make_dict(message : list)->dict: ## return a dict. object with specific arrange
    out = {}
    for item in message:
        out[item[1:]] = item[0]
    return out

def sort_by_key(d: dict)->list:
    l = []
    for item in d.keys():
        l.append(int(item))
    l.sort()
    b = [str(item) for item in l]
    return b

string = 'T4 l16 _36 510 _27 s26 _11 320 414 {6 }39 C2 T0 m28 317 y35 d31 F1 m22 g19 d38 z34 423 l15 329 c12 ;37 19 h13 _30 F5 t7 C3 325 z33 _21 h8 n18 132 k24'

message_chars = string.split(' ')
chars = make_dict(message_chars)
message = ''

for item in sort_by_key(chars):
    message += chars[item]
print(message)





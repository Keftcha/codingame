var MESSAGE = readline();

var liste_message = MESSAGE.split("")

var liste_message_bin = []

for (var idx = 0; idx < liste_message.length;  idx += 1) {
    liste_message_bin.push((liste_message[idx].charCodeAt()).toString(2))
}

for (var idx = 0; idx < liste_message.length; idx += 1) {
    if (liste_message_bin[idx].length < 7) {
        liste_message_bin[idx] = liste_message_bin[idx].split("")
        liste_message_bin[idx].splice(0, 0, "0")
        liste_message_bin[idx] = liste_message_bin[idx].join("")
    }
}

liste_message_bin = liste_message_bin.join("")

function changement_idx(liste) {
    var liste_idx_changement = [0]
    var idx = 0
    while (idx < liste.length - 1) {
        idx += 1
        if (liste[idx - 1] !== liste[idx]) {
            liste_idx_changement.push(idx)
        }
    }
    liste_idx_changement.push(liste.length)
    return liste_idx_changement
}

function codage_chuck(liste, liste_changement) {
    var code = []
    var idx = 0
    var idx_ch = 0
    while (idx < liste.length) {
        if (liste[idx] === "1") {
            code.push("0")
        } else {
            code.push("00")
        }
        var nb_char = Math.abs(liste_changement[idx_ch] -
liste_changement[idx_ch + 1])
        var liste_char = []
        for (var i = 0; i < nb_char; i += 1) {
            liste_char.push("0")
        }
        code.push(liste_char.join(""))
        idx_ch += 1
        idx = liste_changement[idx_ch]
    }
    return code.join(" ")
}

console.log(codage_chuck(liste_message_bin, changement_idx(liste_message_bin)))

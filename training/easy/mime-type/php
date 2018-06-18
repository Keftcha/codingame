<?php
fscanf(STDIN, "%d",
    $N // Number of elements which make up the association table.
);
fscanf(STDIN, "%d",
    $Q // Number Q of file names to be analyzed.
);

$dico_types = array ();

for ($i = 0; $i < $N; $i++)
{
    fscanf(STDIN, "%s %s",
        $EXT, // file extension
        $MT // MIME type.
    );
    $dico_types[strtolower($EXT)] = $MT;
}

$liste_fichiers = array ();

for ($i = 0; $i < $Q; $i++)
{
    $FNAME = stream_get_line(STDIN, 500 + 1, "\n"); // One file name per line.
    $liste_fichiers[] = $FNAME;
}

foreach($liste_fichiers as $fichier)
{
    $extention = strtolower(pathinfo($fichier)["extension"]);
    if (array_key_exists($extention, $dico_types))
    {
        echo $dico_types[$extention] . "\n";
    } else {
        echo "UNKNOWN\n";
    }
}
?>

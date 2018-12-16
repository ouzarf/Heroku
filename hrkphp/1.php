<?php 
echo 'bonjour';

$nom='Mickaël';
$age=17;
$gars=true;
$taille=1.75;

echo'<p>Bonjour à tous.<br/>
Mon vrai nom n\'est pas Toto.<br/>
Mon vrai nom est '.$nom.'<br/>
J\'ai '.$age.' ans et je mesure '.$taille.'m.<br/>
Et comme mon nom l\'indique, je suis ';
if ($gars==true){
echo 'un garçon.</p>';
}
else{
echo 'une fille. </p>';
}

?>
       
       
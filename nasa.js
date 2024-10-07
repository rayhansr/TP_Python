let form = document.getElementById('Form')

form.addEventListener('submit', function(event){
    event.preventDefault();
    let mdp = form.elements['motdepasse'].value;
    let submit = document.getElementById('submit')
    let motdepasse = document.getElementById('motdepasse')
    let motdepase = document.getElementById('mdp')

    if (mdp == "BTSCIEL92110"){
        motdepase.remove()
        motdepasse.remove()
        submit.remove()
        let titre = document.getElementById('titre');
        titre.textContent = 'Voici les codes dacces';
        let rep = document.getElementById('rep')
        rep.textContent = 'VGFGHJ-HJVKG-LJVHKG-BNL9'

    } else{
        alert("Mot de passe incorect")
    }

})
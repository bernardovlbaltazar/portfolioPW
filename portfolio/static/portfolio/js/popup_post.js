
document.addEventListener('DOMContentLoaded', () => {

    document.querySelectorAll('.post').forEach(post => {
        post.onclick = () => {
            document.querySelectorAll('#modal').forEach(modal => {
                if(modal.querySelector('h4').innerHTML === post.querySelector('h4').innerHTML) {
                    if (event.target.nodeName.toLowerCase() != 'a' ) {
                        console.log(event.target.nodeName.toLowerCase());
                        modal.showModal();
                    }

                }
            })
        }
    })
    document.querySelectorAll('.close-button').forEach(button => {
        button.onclick = () => {
            document.querySelectorAll('#modal').forEach(modal => {
                modal.close();
            })
        }
    })

    document.querySelectorAll('.caixa').forEach(caixa => {
        caixa.onclick = () => {
            document.querySelectorAll('#modal').forEach(modal => {
                if(modal.querySelector('h4').innerHTML === caixa.querySelector('h4').innerHTML) {
                    if (event.target.nodeName.toLowerCase() != 'a' ) {
                        console.log(event.target.nodeName.toLowerCase());
                        modal.showModal();
                    }

                }
            })
        }
    })

});

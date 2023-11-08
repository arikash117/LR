const btn = document.querySelector('input')

const lists = document.getElementById('listochki')


btn.onclick = () => {
    console.log('click');
    if (btn.value === 'открыть') {
        lists.style.display = 'block'
        btn.value = 'закрыть'
    } else {
        lists.style.display = 'none'
        btn.value = 'открыть'
    }
}

% import model

<!DOCTYPE html>
<html>

<body>

  <h1>Vislice</h1>

  <blockquote>
    Vislice so najboljša igra za preganjanje dolgčasa (poleg tetrisa).
    <small>Študentje</small>
  </blockquote>
  <table>
    <tr>
        <td>
            <br> <h2>{{igra.pravilni_del_gesla()}}</h2>
        </td>
    </tr>
    
    <tr>
        <td>
            Nepravilni ugibi : {{igra.nepravilni_ugibi()}}
        </td>

        <td>
            Stopnja obešenosti : {{igra.stevilo_napak()}} / {{model.STEVILO_DOVOLJENIH_NAPAK + 1}}
        </td>
    </tr>
</body>

</html>
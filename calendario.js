// Utilize o código abaixo para criação da tabela dCalendario em MS powerBI

let
    MenorData = #date(2021,01,01), //Substitua a data inicial que precisa ser criado
    MaiorData = Date.From(Date.EndOfYear(DateTime.LocalNow())),
    DataInicio = Date.StartOfYear(MenorData),
    DataFim = Date.EndOfYear(MaiorData),
    Dias = Duration.Days(DataFim- DataInicio) +1,
    ListarDatas = List.Dates(DataInicio, Dias, #duration(1,0,0,0)),
    Tabela = #table(
        type table[
            Data = date,
            Dia = Int64.Type,
            Ano = Int64.Type,
            NomeMes = text,
            MesAbre = text,
            MesAno = text,
            MesNum = number,
            AnoMesINT = number,
            Trimestre = Int64.Type,
            TrimestreAbreviado = text,
            Bimestre = text,
            Semestre = text,
            Semana = Int64.Type,
            DiaSemana = Int64.Type,
            NomeDia = text,
            DiaAtualTF = Logical.Type,
            EMesAtualTF = Logical.Type,
            EAnoAtualTF = Logical.Type,
            MesAtual = text,
            AnoAtual = text
            

        ],
        List.Transform(
            ListarDatas,
            each {
                _,
                Date.Day(_),
                Date.Year(_),
                Text.Proper( Date.MonthName(_)),
                Text.Proper(Text.Start(Date.MonthName(_), 3)),
                Text.Proper(Text.Start(Date.MonthName(_), 3)) & "-" & Text.End(Text.From(Date.Year(_)), 2),
                Date.Month(_),
                Date.Year(_) * 100 + Date.Month(_),
                Date.QuarterOfYear(_),
                Text.From(Date.QuarterOfYear(_)) & "º Trim ",
                Text.From( Number.RoundUp( Date.Month(_)/2,0)) & "º Bim",
                Text.From( Number.RoundUp( Date.Month(_)/6,0)) & "º Sem",
                Date.WeekOfMonth(_),
                Date.DayOfWeek(_),
                Date.DayOfWeekName(_),
                Date.IsInCurrentDay(_),
                Date.IsInCurrentMonth(_),
                Date.IsInCurrentYear(_),
                if Date.IsInCurrentMonth(_) and Date.IsInCurrentYear(_) then "Mês Atual" else Text.Proper(Text.Start(Date.MonthName(_), 3)),
                if Date.IsInCurrentYear(_) then "Ano Atual" else Text.From(Date.Year(_))
                

            }

        )
    )
in
    Tabela

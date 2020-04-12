package main

import "fmt"

type Month struct {
	name string
	days int
}

func getMonth(isLeap bool) (month []Month) {
	var febDays int
	if isLeap {
		febDays = 29
	} else {
		febDays = 28
	}

	month = []Month{Month{"Jan", 31},
		Month{"Feb", febDays},
		Month{"Mar", 31},
		Month{"Apr", 30},
		Month{"May", 31},
		Month{"Jun", 30},
		Month{"Jul", 31},
		Month{"Aug", 31},
		Month{"Sep", 30},
		Month{"Oct", 31},
		Month{"Nov", 30},
		Month{"Dec", 31}}
	return
}

type Date struct {
	dayName   string
	month     string
	dayNumber int
}

func (d Date) isBefore(e Date) bool {
	months := []string{"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}

	// The two date are in the same month
	if d.month == e.month {
		return d.dayNumber < e.dayNumber
	}

	for _, m := range months {
		if d.month == m {
			return true
		}
		if e.month == m {
			return false
		}
	}
	return false
}

func (d Date) daysApart(e Date, year []Month) int {
	// Dates are in the same month
	if d.month == e.month {
		return e.dayNumber - d.dayNumber
	}

	daysApart := 0
	for _, m := range year {
		if d.month == m.name {
			daysApart += m.days - d.dayNumber
		} else if e.month == m.name {
			daysApart += e.dayNumber
			break
		} else if d.isBefore(Date{month: m.name, dayNumber: m.days}) {
			daysApart += m.days
		}
	}
	return daysApart
}

func index(slc []string, elem string) int {
	for idx, e := range slc {
		if e == elem {
			return idx
		}
	}
	return -1
}

func main() {
	var leapYear int
	fmt.Scan(&leapYear)

	months := getMonth((leapYear == 1))

	var sourceDayOfWeek, sourceMonth string
	var sourceDayOfMonth int
	fmt.Scan(&sourceDayOfWeek, &sourceMonth, &sourceDayOfMonth)
	initDate := Date{dayName: sourceDayOfWeek, month: sourceMonth, dayNumber: sourceDayOfMonth}

	var targetMonth string
	var targetDayOfMonth int
	fmt.Scan(&targetMonth, &targetDayOfMonth)
	searchDate := Date{month: targetMonth, dayNumber: targetDayOfMonth}

	var dayName string
	if searchDate.isBefore(initDate) {
		days := []string{"Sunday", "Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday"}

		daysApart := searchDate.daysApart(initDate, months)

		dayName = days[(index(days, initDate.dayName)+daysApart)%7]
	} else {
		days := []string{"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}

		daysApart := initDate.daysApart(searchDate, months)

		dayName = days[(index(days, initDate.dayName)+daysApart)%7]
	}

	fmt.Println(dayName)
}

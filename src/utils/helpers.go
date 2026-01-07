package coreengine

import (
	"math"
	"time"
)

const (
	// MinFloat32 represents the minimum value of a float32
	MinFloat32 float32 = math.SmallestNonNaNFloat32
	// MaxFloat32 represents the maximum value of a float32
	MaxFloat32 float32 = math.MaxFloat32
	// Epsilon represents a small value used for floating point comparisons
	Epsilon float64 = 1e-6
)

// DateRange represents a range of dates
type DateRange struct {
	StartDate time.Time
	EndDate   time.Time
}

// NewDateRange returns a new DateRange object
func NewDateRange(startDate, endDate time.Time) *DateRange {
	return &DateRange{
		StartDate: startDate,
		EndDate:   endDate,
	}
}
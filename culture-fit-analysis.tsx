import React from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';

const CultureFitAnalysis = () => {
  const employeeBaseline = {
    purpose: {
      values: "Patient-centered care, making smiles about more than teeth",
      passion: "Pride in providing exceptional care and education", 
      vision: "Creating lasting positive impact on patients' lives"
    },
    people: {
      vibe: "Supportive, collaborative, family-like atmosphere",
      team: "Strong emphasis on teamwork and mutual support",
      association: "Deep connection to colleagues and workplace"
    },
    priorities: {
      time: "Work-life balance, efficient patient care",
      impact: "Patient satisfaction and health outcomes",
      growth: "Professional development and continuous improvement"
    }
  };

  const candidates = [
    {
      name: "Ariele Retherford",
      email: "ariele.retherford@outlook.com",
      scores: {
        purpose: 8,
        people: 9,
        priorities: 9
      },
      highlights: {
        purpose: "Passionate about coordinating and building career impact",
        people: "Strong team collaboration and communication skills",
        priorities: "Proactive in personal development and time management"
      }
    },
    {
      name: "Rajae Penrod",
      email: "rajaestock@yahoo.com",
      scores: {
        purpose: 9,
        people: 8,
        priorities: 8
      },
      highlights: {
        purpose: "12 years dental experience with focus on patient care",
        people: "Values team achievement and collaborative success",
        priorities: "Strong work-life balance and emergency response"
      }
    },
    {
      name: "Kimberlee Talbot",
      email: "kimberleetalbot18@gmail.com",
      scores: {
        purpose: 8,
        people: 8,
        priorities: 8
      },
      highlights: {
        purpose: "Genuine interest in dentistry since high school",
        people: "Shows empathy and understanding with colleagues",
        priorities: "Balanced approach to urgent tasks and family time"
      }
    },
    {
      name: "Brianna Cuevas",
      email: "briannacuevastate@gmail.com",
      scores: {
        purpose: 8,
        people: 8,
        priorities: 8
      },
      highlights: {
        purpose: "Focus on creating positive impact and helping others",
        people: "Strong communication and team management skills",
        priorities: "Demonstrates consideration and work-life balance"
      }
    },
    {
      name: "Liberty Burghardt",
      email: "bewentzecl@gmail.com",
      scores: {
        purpose: 7,
        people: 9,
        priorities: 8
      },
      highlights: {
        purpose: "Creative problem-solver with customer focus",
        people: "Excellence in collaborative environments",
        priorities: "Strong organizational and planning skills"
      }
    },
    {
      name: "Nyla Rattanakone",
      email: "nylarattanakone@gmail.com",
      scores: {
        purpose: 7,
        people: 8,
        priorities: 8
      },
      highlights: {
        purpose: "Customer service focused with pride in service quality",
        people: "Experience managing high-pressure team situations",
        priorities: "Strong work ethic and adaptability"
      }
    },
    {
      name: "Yamileth Moreno",
      email: "yamilethvargas2003@gmail.com",
      scores: {
        purpose: 7,
        people: 8,
        priorities: 8
      },
      highlights: {
        purpose: "Strong customer service and communication skills",
        people: "Thrives in team environments during high-stress periods",
        priorities: "Shows initiative and responsibility"
      }
    },
    {
      name: "Andrea Escobar",
      email: "andrea79609@gmail.com",
      scores: {
        purpose: 8,
        people: 7,
        priorities: 8
      },
      highlights: {
        purpose: "Passionate about helping patients feel confident",
        people: "Strong communication and problem-solving skills",
        priorities: "Shows adaptability and initiative"
      }
    },
    {
      name: "Savanna Pratt",
      email: "Aviepratt8@gmail.com",
      scores: {
        purpose: 7,
        people: 8,
        priorities: 7
      },
      highlights: {
        purpose: "Focus on developing communication skills",
        people: "Values supportive team environment",
        priorities: "Shows initiative in time management"
      }
    },
    {
      name: "Chelsea Antonson",
      email: "chelsea.antonson@gmail.com",
      scores: {
        purpose: 7,
        people: 8,
        priorities: 7
      },
      highlights: {
        purpose: "Passion for teaching and learning from others",
        people: "Creates positive work environments",
        priorities: "Strong work ethic and dedication"
      }
    },
    {
      name: "Cheri Moody",
      email: "cheri4443@gmail.com",
      scores: {
        purpose: 8,
        people: 7,
        priorities: 7
      },
      highlights: {
        purpose: "Strong interest in medical field and helping others",
        people: "Values teamwork and direct communication",
        priorities: "Demonstrates commitment to deadlines"
      }
    },
    {
      name: "Jalizah Kelley",
      email: "Kelleyjalizah@gmail.com",
      scores: {
        purpose: 7,
        people: 7,
        priorities: 8
      },
      highlights: {
        purpose: "Seeking growth opportunities and new experiences",
        people: "Professional approach to team dynamics",
        priorities: "Strong initiative in skill development"
      }
    },
    {
      name: "Israel Andaverde",
      email: "Andaverdeisrael@gmail.com",
      scores: {
        purpose: 7,
        people: 7,
        priorities: 7
      },
      highlights: {
        purpose: "Shows initiative and attention to detail",
        people: "Values authentic team relationships",
        priorities: "Demonstrates proactive work ethic"
      }
    },
    {
      name: "Kamaria James",
      email: "kamariamichelle10@gmail.com",
      scores: {
        purpose: 7,
        people: 7,
        priorities: 7
      },
      highlights: {
        purpose: "Family influence in dental field",
        people: "Experience in conflict resolution",
        priorities: "Shows dedication to responsibilities"
      }
    },
    {
      name: "Tiffany Lupton",
      email: "Luptontiffany1011@gmail.com",
      scores: {
        purpose: 8,
        people: 7,
        priorities: 7
      },
      highlights: {
        purpose: "19 years dental assisting experience",
        people: "Values cross-training and team learning",
        priorities: "Seeks professional growth opportunities"
      }
    },
    {
      name: "Adrianna Camacho",
      email: "adriannacamacho13@gmail.com",
      scores: {
        purpose: 7,
        people: 7,
        priorities: 7
      },
      highlights: {
        purpose: "Committed to specialized patient experience",
        people: "Inspired by compassionate team environments",
        priorities: "Motivated to contribute to team success"
      }
    },
    {
      name: "Isela Lopez",
      email: "lopezisela123@icloud.com",
      scores: {
        purpose: "NA",
        people: "NA",
        priorities: "NA"
      },
      highlights: {
        purpose: "Insufficient information provided",
        people: "Unable to assess team compatibility",
        priorities: "Need more details on work style"
      }
    },
    {
      name: "Hailey Raya",
      email: "haileyyazmin@gmail.com",
      scores: {
        purpose: "NA",
        people: "NA",
        priorities: "NA"
      },
      highlights: {
        purpose: "Insufficient information provided",
        people: "Limited data on team interaction style",
        priorities: "Need more details on work priorities"
      }
    },
    {
      name: "Anniss",
      scores: {
        purpose: "NA",
        people: "NA",
        priorities: "NA"
      },
      highlights: {
        purpose: "No detailed information provided",
        people: "Unable to assess team compatibility",
        priorities: "Insufficient data on work approach"
      }
    },
    {
      name: "Jeff Galica",
      email: "Jgalica27@gmail.com",
      scores: {
        purpose: "NA",
        people: "NA",
        priorities: "NA"
      },
      highlights: {
        purpose: "Limited information available",
        people: "Insufficient data on team interaction",
        priorities: "Need more details on work style"
      }
    },
    {
      name: "Tanya",
      scores: {
        purpose: "NA",
        people: "NA",
        priorities: "NA"
      },
      highlights: {
        purpose: "No detailed information provided",
        people: "Unable to assess team fit",
        priorities: "Insufficient data for evaluation"
      }
    }
  ].sort((a, b) => {
    const avgA = typeof a.scores.purpose === "number" ? 
      (a.scores.purpose + a.scores.people + a.scores.priorities) / 3 : -1;
    const avgB = typeof b.scores.purpose === "number" ? 
      (b.scores.purpose + b.scores.people + b.scores.priorities) / 3 : -1;
    return avgB - avgA;
  });

  const getScoreColor = (score) => {
    if (score === "NA") return 'bg-gray-100';
    if (score >= 8) return 'bg-green-100';
    if (score >= 6) return 'bg-yellow-100';
    return 'bg-red-100';
  };

  const getAverageScore = (scores) => {
    if (typeof scores.purpose !== "number") return "NA";
    return ((scores.purpose + scores.people + scores.priorities) / 3).toFixed(1);
  };

  return (
    <div className="space-y-6">
      <Card className="w-full">
        <CardHeader>
          <CardTitle>Scheduling Coordinator Culture Fit Analysis (Ranked by Average Score)</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-4">
              <h3 className="font-semibold">Organizational Baseline</h3>
              <div className="grid grid-cols-3 gap-4">
                <div>
                  <h4 className="font-medium">Purpose</h4>
                  <p className="text-sm">{employeeBaseline.purpose.values}</p>
                </div>
                <div>
                  <h4 className="font-medium">People</h4>
                  <p className="text-sm">{employeeBaseline.people.vibe}</p>
                </div>
                <div>
                  <h4 className="font-medium">Priorities</h4>
                  <p className="text-sm">{employeeBaseline.priorities.time}</p>
                </div>
              </div>
            </div>
            
            <div className="space-y-4">
              {candidates.map(candidate => (
                <div key={candidate.name} className="border rounded-lg p-4">
                  <div className="flex justify-between items-center mb-2">
                    <div>
                      <h3 className="font-semibold">{candidate.name}</h3>
                      <p className="text-sm text-gray-600">{candidate.email}</p>
                    </div>
                    <span className="text-sm font-medium">
                      Average: {getAverageScore(candidate.scores)}
                    </span>
                  </div>
                  <div className="grid grid-cols-3 gap-4 mt-2">
                    <div className={`p-2 rounded ${getScoreColor(candidate.scores.purpose)}`}>
                      <p className="font-medium">Purpose: {candidate.scores.purpose}</p>
                      <p className="text-sm">{candidate.highlights.purpose}</p>
                    </div>
                    <div className={`p-2 rounded ${getScoreColor(candidate.scores.people)}`}>
                      <p className="font-medium">People: {candidate.scores.people}</p>
                      <p className="text-sm">{candidate.highlights.people}</p>
                    </div>
                    <div className={`p-2 rounded ${getScoreColor(candidate.scores.priorities)}`}>
                      <p className="font-medium">Priorities: {candidate.scores.priorities}</p>
                      <p className="text-sm">{candidate.highlights.priorities}</p>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default CultureFitAnalysis;

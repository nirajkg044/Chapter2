from google.adk.agents import Agent, SequentialAgent
import datetime
from zoneinfo import ZoneInfo

friend_lookup_agent = Agent(
    name="FriendLookupAgent",
    model="gemini-2.0-flash",
    tools=[], 
    description="Pulls a list of friends who are interested in the field trip",
    instruction="""
    You are a lookup assistant. 
    Pull the list of friends interested in the field trip.
    Mock the data. Return a list of names separated by commas.
    """,
    output_key="friends_list"
)

destination_lookup_agent = Agent(
    name="DestinationLookupAgent",
    model="gemini-2.0-flash",
    tools=[],
    description="Suggests a place for the field trip based on the total friends count",
    instruction="""
    You are a travel coordinator. 
    Based on the 'friends_list' in the context, count the number of friends.
    Suggest a suitable destination. If it's a small group, suggest a local place. 
    If it's a large group, suggest a bigger venue.
    Mock the data. Return the name of the destination.
    """,
    output_key="destination"
)

expense_calculator_agent = Agent(
    name="ExpenseCalculatorAgent",
    model="gemini-2.0-flash",
    tools=[],
    description="Calculates the total expenses required for the trip",
    instruction="""
    You are a financial calculator.
    Use the 'friends_list' and 'destination' from the context to calculate the total cost.
    Mock the data: assign a random cost per person and multiply by the group size.
    Return the total cost as a formatted string (e.g. $150.00).
    """,
    output_key="total_expense"
)

booking_agent = Agent(
    name="BookingAgent",
    model="gemini-2.0-flash",
    tools=[],
    description="Books the field trip location venue and returns a booking number",
    instruction="""
    You are a booking agent.
    Use the 'destination' and 'total_expense' from the context to mock a venue booking.
    Return a generated alphanumeric booking confirmation number.
    """,
    output_key="booking_number"
)

def get_current_time(destination: str) -> dict:
    """Returns the current time at 'destination' city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    if destination.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (f"Sorry, I don't have timezone information for {destination}."),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = f'The current time in {destination} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    return {"status": "success", "report": report}

    # Define the sequence of agents
    root_agent = SequentialAgent(
    name="FieldTripPlannerAgent",
    # model=LiteLlm(AGENT_MODEL),#not needed for SequentialAgent
    description="A comprehensive system that finds friends, suggests destinations, calculates expenses, and books a field trip.",
    sub_agents=[
            friend_lookup_agent,
            destination_lookup_agent,
            expense_calculator_agent,
            booking_agent
    ],
    # instruction="You are a travel planner agent. Help the user plan their trip.",
    # tools=[get_current_time],
)


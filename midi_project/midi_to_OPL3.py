import mido
from utils import map_instrument, channel_allowed, MAX_CHANNELS

def limit_polyphony(track_msgs, max_voices=9):
    """
    Limite le nombre de notes simultanées par canal à max_voices.
    Renvoie une nouvelle liste de messages.
    """
    active_notes = {}
    new_msgs = []

    for msg in track_msgs:
        if msg.type == 'note_on' and msg.velocity > 0:
            chan = msg.channel
            active_notes.setdefault(chan, [])
            active_notes[chan].append(msg)
            # limiter le nombre de notes simultanées
            if len(active_notes[chan]) > max_voices:
                # supprime la note la plus faible (velocity)
                weakest = min(active_notes[chan], key=lambda n: n.velocity)
                active_notes[chan].remove(weakest)
        elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
            chan = msg.channel
            if chan in active_notes:
                # supprimer la note correspondante si présente
                active_notes[chan] = [n for n in active_notes[chan] if n.note != msg.note]

        # ajouter tous les messages autorisés
        new_msgs.append(msg)

    return new_msgs

def simplify_midi(input_file: str, output_file: str):
    """Simplifie un MIDI moderne pour OPL3 / Sound Blaster 16"""
    mid = mido.MidiFile(input_file)
    new_mid = mido.MidiFile()

    for track in mid.tracks:
        new_track = mido.MidiTrack()
        # limiter polyphonie
        track_msgs = limit_polyphony(track)
        for msg in track_msgs:
            if msg.type == 'program_change':
                new_prog = map_instrument(msg.program)
                new_track.append(mido.Message(
                    'program_change',
                    program=new_prog,
                    channel=msg.channel,
                    time=msg.time
                ))
            elif msg.type in ['note_on', 'note_off']:
                if channel_allowed(msg.channel):
                    new_track.append(msg)
            else:
                new_track.append(msg)
        new_mid.tracks.append(new_track)

    new_mid.save(output_file)
    print(f"MIDI simplifié pour OPL3 sauvegardé dans {output_file}")

if __name__ == "__main__":
    simplify_midi("exemples/midi_moderne.mid", "exemples/midi_OPL3.mid")

print(f"Nombre maximum de canaux OPL3 : {MAX_CHANNELS}")
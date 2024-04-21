from aima3.logic import *
kb = FolKB()
def get_sysExpert_result(cart):
    kb.tell(expr('(Processor(High) & Ram(High)  & Storage(Large) & BattryLife(x) & Budget(Luxury)) ==> Laptop(High)'))
    kb.tell(expr('(Processor(High) & Ram(High)  & Storage(Medium) & BattryLife(x) & Budget(Luxury)) ==> Laptop(High)'))
    kb.tell(expr('Processor(High) & Ram(High) & Storage(Large) & BattryLife(x) & Budget(Moderate) ==> Laptop(AlmostHigh)'))
    kb.tell(expr('Processor(High) & Ram(High) & Storage(Medium) & BattryLife(x) & Budget(Moderate) ==> Laptop(AlmostHigh)'))

    kb.tell(expr('Processor(High) & Ram(Medium) & Storage(Large) & BattryLife(Long) & Budget(Luxury) ==> Laptop(High)'))
    kb.tell(expr('Processor(High) & Ram(Medium) & Storage(Large) & BattryLife(Medium) & Budget(Luxury) ==> Laptop(High)'))

    kb.tell(expr('Processor(High) & Ram(Medium) &  Storage(Medium) & BattryLife(x) &  Budget(Luxury) ==> Laptop(AlmostHigh)'))
    kb.tell(expr('Processor(High) & Ram(Medium) &  Storage(Medium) & BattryLife(Long) &  Budget(Moderate) ==> Laptop(AlmostHigh)'))
    kb.tell(expr('Processor(High) & Ram(Medium) &  Storage(Medium) & BattryLife(Medium) &  Budget(luxury) ==> Laptop(AlmostHigh)'))

    kb.tell(expr('Processor(Medium) & Ram(High) & Storage(Large) & BattryLife(Long) & Budget(Luxury) ==> Laptop(High)'))
    kb.tell(expr('Processor(Medium) & Ram(High) & Storage(Large) & BattryLife(Medium) & Budget(Luxury) ==> Laptop(High)'))

    kb.tell(expr('Processor(Medium) & Ram(Medium) & Storage(x) & BattryLife(x) & Budget(Moderate) ==> Laptop(Medium)'))
    kb.tell(expr('Processor(Medium) & Ram(High) & Storage(Medium) & BattryLife(x) & Budget(Moderate) ==> Laptop(Meduim)'))
    kb.tell(expr('Processor(Medium) & Ram(Meduim) & Storage(Large) & BattryLife(x) & Budget(Luxury) ==> Laptop(AlmostHigh)'))
    kb.tell(expr('Processor(Medium) & Ram(Meduim) & Storage(Meduim) & BattryLife(long) & Budget(Luxury) ==> Laptop(AlmostHigh)'))

    kb.tell(expr('Processor(Medium) & Ram(Meduim) & Storage(Meduim) & BattryLife(x)  & Budget(Economic) ==> Laptop(AlmostLow)'))
    kb.tell(expr('Processor(Medium) & Ram(Meduim) & Storage(Small)  & BattryLife(x) & Budget(Economic) ==> Laptop(AlmostLow)'))

    kb.tell(expr('Processor(Medium) & Ram(Low) & Storage(Large) & BattryLife(x)) & Budget(Moderate) ==> Laptop(Medium)'))
    kb.tell(expr('Processor(Medium) & Ram(Low) & Storage(Medium) & BattryLife(x) & Budget(Economic) ==> Laptop(AlmostLow)'))
    kb.tell(expr('Processor(Medium) & Ram(Low) & Storage(x) & BattryLife(x) & Budget(Moderate) ==> Laptop(AlmostLow)'))

    kb.tell(expr('Processor(Low) & Ram(Medium) & Storage(small) & BattryLife(x) & Budget(Moderate) ==> Laptop(AlmostLow)'))
    kb.tell(expr('Processor(Low) & Ram(Medium) & Storage(Medium) & BattryLife(x) & Budget(Moderate) ==> Laptop(AlmostLow)'))

    kb.tell(expr('Processor(Low) & Ram(Low) & Storage(x) & BattryLife(x) & Budget(Moderate) ==> Laptop(Low)'))
    kb.tell(expr('Processor(Low) & Ram(Low) & Storage(x) & BattryLife(x) & Budget(Economic) ==> Laptop(Low)'))

    kb.tell(expr('Processor(Low) & Ram(Medium) & Storage(Large) & BattryLife(x) & Budget(Moderate) ==> Laptop(AlmostLow)'))

    agenda = []
    agenda.append(expr(f'Processor({cart.Processor})'))
    agenda.append(expr(f'Ram({cart.Ram})'))
    agenda.append(expr(f'Storage({cart.Storage})'))
    agenda.append(expr(f'BattryLife({cart.BattryLife})'))
    agenda.append(expr(f'Budget({cart.Budget})'))
    memory = {}
    
    seen = set() 
    while agenda:
        elm = agenda.pop(0)

        if elm in seen:
            continue 
        seen.add(elm)
        if fol_fc_ask(kb, elm):
            memory[elm] = True
        else:
            memory[elm] = False

        if memory.get(expr('Processor(High)'), False) and memory.get(expr('Ram(High)'), False) and (memory.get(expr('Storage(Large)')) or memory.get(expr('Storage(Medium)'))) and (memory.get(expr('BattryLife(Medium)')) or memory.get(expr('BattryLife(Long)'))) and memory.get(expr('Budget(Luxury)'), False):
            del memory[expr('Processor(High)')]
            del memory[expr('Ram(High)')]
            if memory.get(expr('Storage(Large)'), False) == True :
                del memory[expr('Storage(Large)')]  
            else: 
                del memory[expr('Storage(Medium)')]
            if memory.get(expr('BattryLife(Medium)'), False) == True: 
                del memory[expr('BattryLife(Medium)')]
            else:
                del memory[expr('BattryLife(Long)')]
            del memory[expr('Budget(Luxury)')]
            agenda.append(expr('Laptop(High)'))

        if memory.get(expr('Processor(High)'), False) and memory.get(expr('Ram(High)'), False) and (memory.get(expr('Storage(Large)')) or memory.get(expr('Storage(Medium)'))) and (memory.get(expr('BattryLife(Medium)')) or memory.get(expr('BattryLife(Long)'))) and memory.get(expr('Budget(Moderate)'), False):
            del memory[expr('Processor(High)')]
            del memory[expr('Ram(High)')]
            if memory.get(expr('Storage(Large)'), False) == True:
                del memory[expr('Storage(Large)')]
            else:
                del memory[expr('Storage(Medium)')]
            if memory.get(expr('BattryLife(Medium)'), False) == True:
                del memory[expr('BattryLife(Medium)')]
            else:
                del memory[expr('BattryLife(Long)')]
            del memory[expr('Budget(Moderate)')]
            agenda.append(expr('Laptop(AlmostHigh)'))

        if memory.get(expr('Processor(High)'), False) and memory.get(expr('Ram(Medium)'), False) and memory.get(expr('Storage(Large)'), False) and (memory.get(expr('BattryLife(Long)'), False) or (memory.get(expr('BattryLife(Medium)'), False) and memory.get(expr('Budget(Luxury)'), False))):
            del memory[expr('Processor(High)')]
            del memory[expr('Ram(Medium)')]
            del memory[expr('Storage(Large)')]
            if memory.get(expr('BattryLife(Long)'), False) == True:
                del memory[expr('BattryLife(Long)')]
            else:
                del memory[expr('BattryLife(Medium)')]
                del memory[expr('Budget(Luxury)')]
            agenda.append(expr('Laptop(High)'))

        if memory.get(expr('Processor(High)'), False) and memory.get(expr('Ram(Medium)'), False) and memory.get(expr('Storage(Medium)'), False) and (memory.get(expr('BattryLife(Long)'), False) or (memory.get(expr('BattryLife(Medium)'), False) and (memory.get(expr('Budget(moderate)'), False) or memory.get(expr('Budget(luxury)'), False)))):
            del memory[expr('Processor(High)')]
            del memory[expr('Ram(Medium)')]
            del memory[expr('Storage(Medium)')]
            if memory.get(expr('BattryLife(Long)'), False) == True:
                del memory[expr('BattryLife(Long)')]
            else:
                del memory[expr('BattryLife(Medium)')]
                if memory.get(expr('Budget(moderate)'), False):
                    del memory[expr('Budget(moderate)')]
                else:
                    del memory[expr('Budget(luxury)')]
            agenda.append(expr('Laptop(AlmostHigh)'))

        if memory.get(expr('Processor(High)'), False) and memory.get(expr('Ram(High)'), False) and (memory.get(expr('Storage(Large)'), False) or memory.get(expr('Storage(Medium)'), False)) and (memory.get(expr('BattryLife(Long)'), False) or (memory.get(expr('BattryLife(Medium)'), False) and memory.get(expr('Budget(Luxury)'), False))):
            del memory[expr('Processor(High)')]
            del memory[expr('Ram(High)')]
            if memory.get(expr('Storage(Large)'), False) == True:
                del memory[expr('Storage(Large)')]
            else:
                del memory[expr('Storage(Medium)')]
            if memory.get(expr('BattryLife(Long)'), False) == True:
                del memory[expr('BattryLife(Long)')]
            else:
                del memory[expr('BattryLife(Medium)')]
                del memory[expr('Budget(Luxury)')]
            agenda.append(expr('Laptop(High)'))

        if memory.get(expr('Processor(Medium)'), False) and memory.get(expr('Ram(High)'), False) and memory.get(expr('Storage(Large)'), False) and (memory.get(expr('BattryLife(Long)'), False) or (memory.get(expr('BattryLife(Medium)'), False) and memory.get(expr('Budget(Luxury)'), False))):
            del memory[expr('Processor(Medium)')]
            del memory[expr('Ram(High)')]
            del memory[expr('Storage(Large)')]
            if memory.get(expr('BattryLife(Long)'), False) == True:
                del memory[expr('BattryLife(Long)')]
            else:
                del memory[expr('BattryLife(Medium)')]
                del memory[expr('Budget(Luxury)')]
            agenda.append(expr('Laptop(High)'))

        if memory.get(expr('Processor(Medium)'), False) and memory.get(expr('Ram(Medium)'), False) and (memory.get(expr('Storage(Large)'), False) or memory.get(expr('Storage(Medium)'), False)) and (memory.get(expr('BattryLife(Long)'), False) or (memory.get(expr('BattryLife(Medium)'), False) and memory.get(expr('Budget(Luxury)'), False))):
            del memory[expr('Processor(Medium)')]
            del memory[expr('Ram(Medium)')]
            if memory.get(expr('Storage(Large)'), False) == True:
                del memory[expr('Storage(Large)')]
            else:
                del memory[expr('Storage(Medium)')]
            if memory.get(expr('BattryLife(Long)'), False) == True:
                del memory[expr('BattryLife(Long)')]
            else:
                del memory[expr('BattryLife(Medium)')]
                del memory[expr('Budget(Luxury)')]
            agenda.append(expr('Laptop(High)'))

        if memory.get(expr('Processor(Medium)'), False) and memory.get(expr('Ram(High)'), False) and memory.get(expr('Storage(Medium)'), False) and (memory.get(expr('BattryLife(Long)'), False) or (memory.get(expr('BattryLife(Medium)'), False) and memory.get(expr('Budget(Moderate)'), False))):
            del memory[expr('Processor(Medium)')]
            del memory[expr('Ram(High)')]
            del memory[expr('Storage(Medium)')]
            if memory.get(expr('BattryLife(Long)'), False) == True:
                del memory[expr('BattryLife(Long)')]
            else:
                del memory[expr('BattryLife(Medium)')]
                del memory[expr('Budget(Moderate)')]
            agenda.append(expr('Laptop(Medium)'))

        if memory.get(expr('Processor(Medium)'), False) and memory.get(expr('Ram(Medium)'), False) and (memory.get(expr('Storage(Large)'), False) or memory.get(expr('Storage(Medium)'), False)) and (memory.get(expr('BattryLife(Long)'), False) or (memory.get(expr('BattryLife(Medium)'), False) and memory.get(expr('Budget(Luxury)'), False))):
            del memory[expr('Processor(Medium)')]
            del memory[expr('Ram(Medium)')]
            if memory.get(expr('Storage(Large)'), False) == True:
                del memory[expr('Storage(Large)')]
            else:
                del memory[expr('Storage(Medium)')]
            if memory.get(expr('BattryLife(Long)'), False) == True:
                del memory[expr('BattryLife(Long)')]
            else:
                del memory[expr('BattryLife(Medium)')]
                del memory[expr('Budget(Luxury)')]
            agenda.append(expr('Laptop(AlmostHigh)'))

        if memory.get(expr('Processor(Medium)'), False) and memory.get(expr('Ram(Medium)'), False) and (memory.get(expr('Storage(Medium)'), False) or memory.get(expr('Storage(Small)'), False)) and (memory.get(expr('BattryLife(Long)'), False) or (memory.get(expr('BattryLife(Medium)'), False) and memory.get(expr('Budget(Economic)'), False))):
            del memory[expr('Processor(Medium)')]
            del memory[expr('Ram(Medium)')]
            if memory.get(expr('Storage(Medium)'), False) == True:
                del memory[expr('Storage(Medium)')]
            else:
                del memory[expr('Storage(Small)')]
            if memory.get(expr('BattryLife(Long)'), False) == True:
                del memory[expr('BattryLife(Long)')]
            else:
                del memory[expr('BattryLife(Medium)')]
                del memory[expr('Budget(Economic)')]
            agenda.append(expr('Laptop(Medium)'))

        if memory.get(expr('Processor(Medium)'), False) and memory.get(expr('Ram(Low)'), False) and (memory.get(expr('Storage(Small)'), False) or memory.get(expr('Storage(Medium)'), False)) and memory.get(expr('BattryLife(x)'), False) and memory.get(expr('Budget(Moderate)'), False):
            del memory[expr('Processor(Medium)')]
            del memory[expr('Ram(Low)')]
            if memory.get(expr('Storage(Small)'), False) == True:
                del memory[expr('Storage(Small)')]
            else:
                del memory[expr('Storage(Medium)')]
            del memory[expr('BattryLife(x)')]
            del memory[expr('Budget(Moderate)')]
            agenda.append(expr('Laptop(Medium)'))

        if memory.get(expr('Processor(Medium)'), False) and memory.get(expr('Ram(Low)'), False) and (memory.get(expr('Storage(Small)'), False) or memory.get(expr('Storage(Medium)'), False)) and memory.get(expr('BattryLife(x)'), False) and memory.get(expr('Budget(Economic)'), False):
            del memory[expr('Processor(Medium)')]
            del memory[expr('Ram(Low)')]
            if memory.get(expr('Storage(Small)'), False) == True:
                del memory[expr('Storage(Small)')]
            else:
                del memory[expr('Storage(Medium)')]
            del memory[expr('BattryLife(x)')]
            del memory[expr('Budget(Economic)')]
            agenda.append(expr('Laptop(AlmostLow)'))

        if memory.get(expr('Processor(Low)'), False) and memory.get(expr('Ram(Medium)'), False) and (memory.get(expr('Storage(Small)'), False) or memory.get(expr('Storage(Medium)'), False)) and memory.get(expr('BattryLife(x)'), False) and memory.get(expr('Budget(Moderate)'), False):
            del memory[expr('Processor(Low)')]
            del memory[expr('Ram(Medium)')]
            if memory.get(expr('Storage(Small)'), False) == True:
                del memory[expr('Storage(Small)')]
            else:
                del memory[expr('Storage(Medium)')]
            del memory[expr('BattryLife(x)')]
            del memory[expr('Budget(Moderate)')]
            agenda.append(expr('Laptop(AlmostLow)'))

        if memory.get(expr('Processor(Low)'), False) and memory.get(expr('Ram(Low)'), False) and (memory.get(expr('Storage(Small)'), False) or memory.get(expr('Storage(Medium)'), False)) and memory.get(expr('BattryLife(x)'), False) and (memory.get(expr('Budget(Moderate)'), False) or memory.get(expr('Budget(Economic)'), False)):
            del memory[expr('Processor(Low)')]
            del memory[expr('Ram(Low)')]
            if memory.get(expr('Storage(Small)'), False) == True:
                del memory[expr('Storage(Small)')]
            else:
                del memory[expr('Storage(Medium)')]
            del memory[expr('BattryLife(x)')]
            if memory.get(expr('Budget(Moderate)'), False) == True:
                del memory[expr('Budget(Moderate)')]
            else:
                del memory[expr('Budget(Economic)')]
            agenda.append(expr('Laptop(Low)'))

        if memory.get(expr('Processor(Low)'), False) and memory.get(expr('Ram(Medium)'), False) and memory.get(expr('Storage(Large)'), False) and memory.get(expr('BattryLife(x)'), False) and memory.get(expr('Budget(Moderate)'), False):
            del memory[expr('Processor(Low)')]
            del memory[expr('Ram(Medium)')]
            del memory[expr('Storage(Large)')]
            del memory[expr('BattryLife(x)')]
            del memory[expr('Budget(Moderate)')]
            agenda.append(expr('Laptop(AlmostLow)'))

    print('Final diagnosis:')
    for p, value in memory.items():
        if value:
            print(f'{p}') 